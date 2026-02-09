#!/usr/bin/env bash
set -euo pipefail

# Gemini TTS - Generate speech using Gemini 2.5 TTS models
# Usage: ./gemini-tts.sh "text to speak" VoiceName [output.wav]

# Load API key
if [[ -f ~/.openclaw/secrets.env ]]; then
    source ~/.openclaw/secrets.env
fi

if [[ -z "${GEMINI_API_KEY:-}" ]]; then
    echo "ERROR: GEMINI_API_KEY not set in ~/.openclaw/secrets.env" >&2
    exit 1
fi

# Defaults
MODEL="gemini-2.5-flash-preview-tts"
OUTPUT="out.wav"
MULTI_SPEAKER=false

# Parse arguments
if [[ $# -lt 2 ]]; then
    echo "Usage: $0 \"text to speak\" VoiceName [output.wav]" >&2
    echo "       $0 \"conversation\" --multi Voice1,Voice2 Speaker1,Speaker2 [output.wav]" >&2
    echo "" >&2
    echo "Examples:" >&2
    echo "  $0 'Say cheerfully: Have a great day!' Kore" >&2
    echo "  $0 'Joe: Hi! Jane: Hello!' --multi Kore,Puck Joe,Jane podcast.wav" >&2
    exit 1
fi

TEXT="$1"
shift

# Check for multi-speaker mode
if [[ "${1:-}" == "--multi" ]]; then
    MULTI_SPEAKER=true
    shift
    
    if [[ $# -lt 2 ]]; then
        echo "ERROR: --multi requires Voice1,Voice2 Speaker1,Speaker2" >&2
        exit 1
    fi
    
    IFS=',' read -r VOICE1 VOICE2 <<< "$1"
    shift
    IFS=',' read -r SPEAKER1 SPEAKER2 <<< "$1"
    shift
    
    if [[ -n "${1:-}" ]]; then
        OUTPUT="$1"
    fi
else
    VOICE_NAME="$1"
    if [[ -n "${2:-}" ]]; then
        OUTPUT="$2"
    fi
fi

# Create temporary files
TMP_RESPONSE=$(mktemp)
TMP_PCM=$(mktemp)
trap "rm -f '$TMP_RESPONSE' '$TMP_PCM'" EXIT

# Build request JSON
if [[ "$MULTI_SPEAKER" == "true" ]]; then
    REQUEST_JSON=$(cat <<EOF
{
  "contents": [{
    "parts":[{
      "text": $(jq -Rs . <<< "$TEXT")
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [
          {
            "speaker": "$SPEAKER1",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "$VOICE1"
              }
            }
          },
          {
            "speaker": "$SPEAKER2",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "$VOICE2"
              }
            }
          }
        ]
      }
    }
  }
}
EOF
)
else
    REQUEST_JSON=$(cat <<EOF
{
  "contents": [{
    "parts":[{
      "text": $(jq -Rs . <<< "$TEXT")
    }]
  }],
  "generationConfig": {
    "responseModalities": ["AUDIO"],
    "speechConfig": {
      "voiceConfig": {
        "prebuiltVoiceConfig": {
          "voiceName": "$VOICE_NAME"
        }
      }
    }
  }
}
EOF
)
fi

# Call Gemini TTS API
echo "🎙️  Generating speech with Gemini TTS..." >&2
echo "   Model: $MODEL" >&2
if [[ "$MULTI_SPEAKER" == "true" ]]; then
    echo "   Voices: $VOICE1 ($SPEAKER1), $VOICE2 ($SPEAKER2)" >&2
else
    echo "   Voice: $VOICE_NAME" >&2
fi
echo "   Output: $OUTPUT" >&2

HTTP_CODE=$(curl -w "%{http_code}" -o "$TMP_RESPONSE" -s \
    "https://generativelanguage.googleapis.com/v1beta/models/$MODEL:generateContent" \
    -H "x-goog-api-key: $GEMINI_API_KEY" \
    -H "Content-Type: application/json" \
    -X POST \
    -d "$REQUEST_JSON")

if [[ "$HTTP_CODE" != "200" ]]; then
    echo "❌ API request failed with HTTP $HTTP_CODE" >&2
    echo "Response:" >&2
    cat "$TMP_RESPONSE" >&2
    exit 1
fi

# Extract base64 audio data
AUDIO_DATA=$(jq -r '.candidates[0].content.parts[0].inlineData.data' "$TMP_RESPONSE")

if [[ "$AUDIO_DATA" == "null" || -z "$AUDIO_DATA" ]]; then
    echo "❌ No audio data in response" >&2
    echo "Response:" >&2
    cat "$TMP_RESPONSE" >&2
    exit 1
fi

# Decode base64 to PCM
echo "$AUDIO_DATA" | base64 --decode > "$TMP_PCM"

# Check if ffmpeg is available
if ! command -v ffmpeg &> /dev/null; then
    echo "⚠️  ffmpeg not found, saving as raw PCM: ${OUTPUT%.wav}.pcm" >&2
    cp "$TMP_PCM" "${OUTPUT%.wav}.pcm"
    echo "✅ Audio saved: ${OUTPUT%.wav}.pcm" >&2
    echo "   To convert: ffmpeg -f s16le -ar 24000 -ac 1 -i ${OUTPUT%.wav}.pcm $OUTPUT" >&2
    exit 0
fi

# Convert PCM to WAV using ffmpeg
ffmpeg -f s16le -ar 24000 -ac 1 -i "$TMP_PCM" -y "$OUTPUT" -loglevel error

if [[ -f "$OUTPUT" ]]; then
    SIZE=$(du -h "$OUTPUT" | cut -f1)
    echo "✅ Audio generated: $OUTPUT ($SIZE)" >&2
else
    echo "❌ Failed to create output file" >&2
    exit 1
fi
