import platform

# For Windows -->
if platform.system() == "Windows":
    import pyttsx3
    try:
        engine = pyttsx3.init()
    except ImportError as e:
        print(e)
    except RuntimeError as e:
        print(e)
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 140)

    def speak_text(txt):
        engine.say(txt)
        engine.runAndWait()

#For Mac / Linux
if platform.system() == "Darwin" or platform.system() == "Linux":
    import os

    def speak_text(txt):
        txt = txt.replace('"','')
        txt = txt.replace("'","")
        os.system(f'gtts-cli --nocheck "{texts}" | mpg123 -q -')

def print_say(txt):
    speak_text(txt)
    print(txt)

