import platform



def jinput():
    if platform.system() == "Windows":
        import speech_recognition as sr
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio, language ='en-in')
            print(f"User said: {text}\n")
        except Exception as e:
            print(e)
            print("Unable to proccess voice.")
            text = "pass"
    else:
        text = input(">>")
    return text