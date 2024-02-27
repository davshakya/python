import threading
import time
import threading
import time
import pyttsx3
import speech_recognition as sr

def print_numbers():
    engine = pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 125)
    engine.setProperty('volume',0.2)
    engine.say("Hello, How are you?,Speechnotes is a reliable and secure web-based speech-to-text tool that enables you to quickly and accurately transcribe your audio and video recordings, as well as dictate your notes instead of typing, saving you time and effort. With features like voice commands for punctuation and formatting, automatic capitalization, and easy import/export options, Speechnotes provides an efficient and user-friendly dictation and transcription experience. Proudly serving millions of users since 2015, Speechnotes is the go-to tool for anyone who needs fast, accurate & private transcription.")
    engine.save_to_file('Hello World', 'test.mp3') 
    engine.runAndWait()

def print_letters():
    for i in range(15):
        time.sleep(1)
        print(f"Thread 1: {i}")
# Create two threads
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")
