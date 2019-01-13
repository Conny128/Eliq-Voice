import requests
import json
import time

#from gtts import gTTS
#import os
#gTTS(text='Good morning', lang='en')

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello from Eliq")

Eliq_list = []
power_value = 0
power_value_int = 0
prompt=0
Eliq_just_NOW ={}
accesstoken = "xxxxxxxxxxxxxxxxxxxxxx"

prompt = input ("What is the warning limit in Watts: ") #Say warning for power use over this limmit in Watts
level_warning = int(prompt)

prompt = input ("How many minutes between each? : ")
offset_tid=int(prompt)

Eliq_request_string = ('https://my.eliq.io/api/datanow?accesstoken={}&channelid=32217'.format(accesstoken))

while True:
    response = requests.get (Eliq_request_string)
    Eliq_just_NOW = (response.json())
    power_value = Eliq_just_NOW['power']
    power_value_int = int (float (power_value))
    power_str = (f'Power is {power_value_int} Watts') 
    
    print (power_str)
   
    if power_value_int > level_warning:
        speak.Speak(power_str)
        speak.Speak ("Warning!")
    else:
        speak.Speak(power_str)
        speak.Speak ("Good!")
        
    time.sleep(offset_tid*60)
    
