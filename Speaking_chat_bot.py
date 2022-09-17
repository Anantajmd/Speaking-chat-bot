# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 02:12:35 2022

@author: Ananta Jamdhade
Description : This is speaking chat bot.
              Press 'a' key on keyboard to speek
              Press 'q' key for exit
"""

import openai
import pyttsx3
import speech_recognition as sr
import keyboard

engine = pyttsx3.init()
flag = 0
r = sr.Recognizer()
#store the openai api key in the file OPENAI_API_KEY.txt in current folder 
openai.api_key_path = "./OPENAI_API_KEY.txt"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "

print("This is the GPT-3 AI how I an help you")
while True:
    if keyboard.is_pressed("a"):
        #print("You pressed 'a' \n")
        with sr.Microphone() as source:
            print("AI said  : How I can help you \n")
            audio = r.listen(source)  
            try:
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
                question = text
                flag = 1
            except:
                print("Sorry could not recognize what you said")
    if flag:
        response = openai.Completion.create(
          #model="text-curie-001",
          model="text-davinci-002",
          prompt=question,
          temperature=0.9,
          max_tokens=150,
          top_p=1,
          frequency_penalty=0,
          presence_penalty=0.6,
          stop=[" Human:", " AI:"]
        )
        print("AI said  : " + response.choices[0]["text"])
        engine.say(response.choices[0]["text"])
        engine.runAndWait()
        flag = 0
        
    if keyboard.is_pressed("q"):
        break
    



