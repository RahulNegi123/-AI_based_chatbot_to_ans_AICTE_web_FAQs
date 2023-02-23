## rasa run -m models --endpoints endpoints.yml --port 5002 --credentials credentials.yml
import requests
import speech_recognition as sr
import subprocess
import os
from playsound import playsound

from gtts import gTTS
bot_message = ""
message=""
r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": "Hello"})
print("Bot says, ",end=' ')
for i in r.json():
    bot_message = i['text']
    print(f"{bot_message}")

myobj = gTTS(text=bot_message)
myobj.save("welcome.mp3")
print('saved')
# Playing the converted file
#subprocess.call(['xdg-open', '/home/PycharmProjects/Rasa_chatbot/rasaChat/welcome.mp3'])
playsound("welcome.mp3")
while bot_message != "Bye" or bot_message!='thanks':
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            message = r.recognize_google(audio)
            print("You said : {}".format(message))

        except:
            print("Sorry could not recognize your voice")
    if len(message)==0:
        continue
    print("Sending message now...")

    r = requests.post('http://localhost:5002/webhooks/rest/webhook', json={"message": message})

    print("Bot says, ",end=' ')
    for i in r.json():
        bot_message = i['text']
        print(f"{bot_message}")

    myobj = gTTS(text=bot_message)
    myobj.save("welcome.mp3")
    print('saved')
    # Playing the converted file
    #subprocess.call(['xdg-open', '/home/PycharmProjects/Rasa_chatbot/rasaChat/welcome.mp3'])
    playsound("welcome.mp3")

