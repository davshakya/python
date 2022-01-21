import pyttsx3
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 125)
engine.setProperty('volume',0.2)
engine.say("Hello, How are you?")
engine.save_to_file('Hello World', 'test.mp3') 
engine.runAndWait()









 



