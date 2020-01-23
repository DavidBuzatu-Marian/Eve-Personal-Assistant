import speech_recognition as sr
import webbrowser
import time
import playsound
import os
import random
import subprocess
from gtts import gTTS

from time import ctime

recognizer = sr.Recognizer()


def save_file_to_git():
    p = subprocess.Popen("C:\Progra~1\Git\git-bash.exe ./shellGitSave.sh",
                         bufsize=-1,
                         executable=None,
                         stdin=None,
                         stdout=None,
                         stderr=None,
                         preexec_fn=None,
                         close_fds=False,
                         shell=True,
                         cwd="E:\Projects\Python-Assistant",
                         )
    p.wait()


def record_audio(source, ask=False):
    if ask:
        alexis_speak(ask)
    audio = recognizer.listen(source)
    voice_data = ''
    try:
        voice_data = recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        alexis_speak('Sorry, I did not get that')
    except sr.RequestError:
        alexis_speak('Sorry, service is down')
    return voice_data


def alexis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    randomString = random.randint(1, 10000000)
    audio_file = 'audio-' + str(randomString) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(source, voice_data):
    if 'what is your name' in voice_data:
        alexis_speak('My name is Alexis')
    if 'what time is it' in voice_data:
        alexis_speak(ctime())
    if 'search' in voice_data:
        search = record_audio(source, 'What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        alexis_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio(source, 'What is the location')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        alexis_speak('Here is the location of ' + location)
    if 'save' in voice_data:
        alexis.speak('Saving')
        save_file_to_git()
    if 'exit' in voice_data:
        exit()


time.sleep(1)
save_file_to_git()
# alexis_speak('How can I help you?')
# with sr.Microphone() as source:
#     while 1:
#         voice_data = record_audio(source)
#         respond(source, voice_data)
#         recognizer.adjust_for_ambient_noise(source, 0.5)
