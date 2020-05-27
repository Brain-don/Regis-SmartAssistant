import time
import os
from gtts import gTTS


def regis(audio):
    speech = gTTS(text=audio, lang='en', slow=False)

    speech.save("tts.mp3")
    os.system("start tts.mp3")
    print(audio)
    time.sleep(1.5)
    os.remove("tts.mp3")
