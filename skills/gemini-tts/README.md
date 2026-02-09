# Gemini TTS Skill

High-quality text-to-speech using Gemini 2.5 models.

## Quick Start

```bash
# Simple TTS
./gemini-tts.sh "Olá! Bem-vindo ao Gemini TTS." Kore

# With emotion
./gemini-tts.sh "Say excitedly: This is amazing!" Puck test.wav

# Multi-speaker conversation
./gemini-tts.sh "Joe: Hi there! Jane: Hello Joe!" --multi Kore,Puck Joe,Jane conversation.wav
```

## Why Use This?

**vs OpenClaw Edge TTS (default):**
- ✅ Better quality (Gemini models trained on natural speech)
- ✅ Natural language control ("say cheerfully", "whisper", etc.)
- ✅ Multi-speaker in one call
- ✅ 30 different voice personalities
- ❌ Requires API key (not free)
- ❌ Slower (API call vs local)

**vs OpenAI TTS:**
- ✅ More voice options (30 vs 6)
- ✅ Natural language prompt control
- ✅ Multi-speaker native support
- ✅ 100+ languages auto-detected
- ≈ Similar quality
- ≈ Similar pricing

**vs ElevenLabs:**
- ❌ Less control than ElevenLabs Pro
- ✅ Cheaper
- ✅ No rate limits on paid tier
- ≈ Similar quality on standard voices

## Voice Recommendations

**For podcast/storytelling:** Kore (firm), Charon (informative)
**For upbeat content:** Puck, Zephyr, Aoede
**For emotional range:** Enceladus (breathy), Fenrir (excitable)
**For news/formal:** Charon, Rasalgethi

## Test It

```bash
# Portuguese test
./gemini-tts.sh "Fala pessoal! Hoje vamos testar o TTS do Gemini." Kore gemini-pt-test.wav

# English emotional test
./gemini-tts.sh "Say sadly: I can't believe it's over..." Enceladus sad-test.wav

# Multi-speaker podcast intro
./gemini-tts.sh "Franklin: Bem-vindo ao podcast! 
Funes: Opa! Vamos conversar sobre IA." --multi Kore,Puck Franklin,Funes podcast-intro.wav
```

## Integration Notes

This skill is **standalone** - it works via CLI. To integrate with OpenClaw's `tts` tool, we'd need to:
1. Create OpenClaw TTS provider plugin
2. Register `gemini-tts` as provider
3. Configure in gateway config

For now, use directly via exec:
```javascript
exec(`cd ${skillPath} && ./gemini-tts.sh "${text}" Kore output.wav`)
```

See `SKILL.md` for full documentation.
