import requests
import json
import time

#from gtts import gTTS
#import os
#gTTS(text='Good morning', lang='en')

import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello World")

power_value = 0
power_value_int = 0
prompt=0
Eliq_just_NOW ={}

print ("How many minutes interval (recomended 10 minutes)? : ")
prompt=input()
offset_tid=int(prompt)

for i in range (offset_tid):
    response = requests.get ("https://my.eliq.io/api/datanow?accesstoken=aaaaaaaaaaaaaaaaaaaa&channelid=ccccc")
    Eliq_just_NOW = (response.json())
    power_value = Eliq_just_NOW['power']
    power_value_int = int (float (power_value))
    power_str = (f'Power is {power_value_int} Watts') 
    
    
    if power_value_int >= 2000:
        print (power_str)
        speak.Speak(power_str)
        speak.Speak ("Warning!")
    else:
        print (power_str)
        speak.Speak(power_str)
        speak.Speak ("Good!")
        
    time.sleep(60)
    
