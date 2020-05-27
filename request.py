import speech_recognition as sr


def myCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)
        print('Say something...')
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio).lower()
        print(f'You said: {command} \n')
    # speech is unrecognizable. loop back to listening
    except sr.UnknownValueError:
        print('.....')
        command = myCommand()
    return command
