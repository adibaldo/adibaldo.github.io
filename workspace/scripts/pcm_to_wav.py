import wave
import sys

def pcm_to_wav(pcm_file, wav_file):
    with open(pcm_file, 'rb') as pcm:
        pcm_data = pcm.read()
        with wave.open(wav_file, 'wb') as wav:
            wav.setnchannels(1)
            wav.setsampwidth(2)
            wav.setframerate(24000)
            wav.writeframes(pcm_data)

if __name__ == "__main__":
    pcm_to_wav(sys.argv[1], sys.argv[2])
