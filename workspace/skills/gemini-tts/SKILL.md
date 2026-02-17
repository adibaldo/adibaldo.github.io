# Gemini TTS Skill

Generate high-quality text-to-speech audio using Google's Gemini 2.5 TTS models.

## Features

- **30 voice options** with different personalities (Kore, Puck, Zephyr, etc.)
- **Multi-speaker support** (up to 2 speakers in one audio)
- **Natural language control** - describe how you want it to sound
- **100+ languages** including Portuguese
- **Controllable style** - emotion, accent, pace, tone via prompts

## Prerequisites

- Gemini API key in `~/.openclaw/secrets.env`:
  ```bash
  export GEMINI_API_KEY="AIzaSy..."
  ```

## Usage

### Single Speaker

```bash
./gemini-tts.sh "Say cheerfully: Have a wonderful day!" Kore
```

Output: `out.wav` in current directory

### Multi-Speaker (Conversation)

```bash
./gemini-tts.sh "TTS the following conversation between Joe and Jane:
Joe: How's it going today Jane?
Jane: Not too bad, how about you?" --multi Kore,Puck Joe,Jane
```

### With Style Control

```bash
./gemini-tts.sh "Say in a spooky whisper: By the pricking of my thumbs... Something wicked this way comes" Enceladus
```

### Advanced: Custom Prompt

For complex performances, use the prompting structure from docs:

```bash
cat > podcast-script.txt << 'EOF'
# AUDIO PROFILE: Jaz R.
## "The Morning Hype"

## THE SCENE: The London Studio
It is 10:00 PM in a glass-walled studio overlooking the moonlit London skyline...

### DIRECTOR'S NOTES
Style: The "Vocal Smile" - bright, sunny, inviting
Pace: Energetic pace, bouncing cadence
Accent: Brixton, London

#### TRANSCRIPT
Yes, massive vibes in the studio! You are locked in and it is absolutely popping off...
EOF

./gemini-tts.sh "$(cat podcast-script.txt)" Kore
```

## Voice Options

**Bright/Upbeat:**
- Zephyr (Bright), Puck (Upbeat), Aoede (Breezy), Autonoe (Bright), Laomedeia (Upbeat)

**Firm/Clear:**
- Kore (Firm), Orus (Firm), Iapetus (Clear), Erinome (Clear), Alnilam (Firm)

**Smooth/Easy-going:**
- Callirrhoe (Easy-going), Umbriel (Easy-going), Algieba (Smooth), Despina (Smooth)

**Informative:**
- Charon (Informative), Rasalgethi (Informative)

**Special:**
- Enceladus (Breathy), Algenib (Gravelly), Fenrir (Excitable), Gacrux (Mature)

Full list: https://ai.google.dev/gemini-api/docs/speech-generation#voices

## Models

- `gemini-2.5-flash-preview-tts` (default) - Fast, cheap
- `gemini-2.5-pro-preview-tts` - Higher quality (slower, more expensive)

## Limitations

- Max 32k tokens per request
- Audio output only (can't return text + audio)
- Multi-speaker limited to 2 speakers

## Examples

### Brazilian Portuguese Podcast

```bash
./gemini-tts.sh "Olá pessoal! Bem-vindos ao nosso podcast de tecnologia. Hoje vamos falar sobre inteligência artificial." Kore
```

### News Report Style

```bash
./gemini-tts.sh "Say in a serious news anchor voice: Breaking news from the technology sector today..." Charon
```

### Emotional Range

```bash
# Excited
./gemini-tts.sh "Say excitedly: OH MY GOD THIS IS AMAZING!" Fenrir

# Sad
./gemini-tts.sh "Say sadly: I can't believe it's over..." Enceladus

# Angry
./gemini-tts.sh "Say angrily: This is completely unacceptable!" Alnilam
```

## Integration with OpenClaw

The skill can be used by OpenClaw's `tts` tool when configured as a provider.

## References

- [Gemini TTS Docs](https://ai.google.dev/gemini-api/docs/speech-generation)
- [AI Studio TTS Generator](https://aistudio.google.com/generate-speech)
- [TTS Cookbook](https://colab.research.google.com/github/google-gemini/cookbook/blob/main/quickstarts/Get_started_TTS.ipynb)
