from moviepy.editor import AudioFileClip
import speech_recognition as sr
from gtts import gTTS
import subprocess
import os
import platform
import time

def play_audio(text, lang='en'):
# Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)
    # Save the audio file
    audio_file = "output.mp3"
    tts.save(audio_file)
    # Play the audio file based on the operating system
    if platform.system() == 'Darwin':
    # macOS
      os.system(f"afplay {audio_file}")
    elif platform.system() == 'Linux':
    # Linux
        os.system(f"mpg321 {audio_file}")
    elif platform.system() == 'Windows':
    # Windows
        os.system(audio_file)
    else:
        print("Unsupported operating system")
        
def close_media_player():
    command = 'taskkill /F /IM Microsoft.Media.Player.exe'
    subprocess.run(command,shell=True)

def convert_mp4_to_wav(mp4_file_path):
    # Extract the audio
    audio_clip = AudioFileClip(mp4_file_path)
    # Save the audio as a WAV file
    audio_clip.write_audiofile("wav_file.wav", codec='pcm_s16le')
        
def audio_to_text(audio_file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file_path) as audio_file:
        audio_data = recognizer.record(audio_file)
    try:
        text = recognizer.recognize_google(audio_data)
        print("Text: {}".format(text))
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None
    
play_audio("hello this is world")
close_media_player()
convert_mp4_to_wav("output.mp3")
audio_to_text("wav_file.wav")


