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
    engine.say("Hello, How are you?")
    engine.save_to_file('Hello World', 'test.mp3') 
    engine.runAndWait()
    import pyaudio

    

def print_letters():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        # Adjust the ambient noise level for better recognition
        recognizer.adjust_for_ambient_noise(source)

        try:
            audio = recognizer.listen(source, timeout=5)
            print("Processing audio...")

            # Use Google Web Speech API to convert audio to text
            text = recognizer.recognize_google(audio)
            print("You said:", text)

        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


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
