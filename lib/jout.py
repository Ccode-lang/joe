import platform

def jout(text):
    if platform.system() == "Windows":
        import pyttsx3
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        
        engine.say(text)
        engine.runAndWait()
    else:
        print(text)