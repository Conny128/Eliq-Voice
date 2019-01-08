import requests
import json
import time


import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
speak.Speak("Hello World")

#from gtts import gTTS
#import os
#gTTS(text='Good morning', lang='en')



Eliq_list = []
power_value = 0
power_value_int = 0
prompt=0

present_time = time.localtime()
print (present_time)
print ("How many minutes interval (recomended 10 minutes)?")
prompt=input()
offset_tid=int(prompt)
min_tid = present_time[4]
print (min_tid)
max_tid = min_tid + offset_tid
print (max_tid)

for i in range (offset_tid):
    print(i)

    response = requests.get ("https://my.eliq.io/api/datanow?accesstoken=xxxxxxxxxxxxxxxxxxxxxx&channelid=yyyyyy")
    
    Eliq_just_NOW_string = str (response.json())
    #print (Eliq_just_NOW_string)
    Eliq_list.insert(0,Eliq_just_NOW_string.split(",")[0])
    Eliq_list.insert(1,Eliq_just_NOW_string.split(",")[1])
    Eliq_list.insert(2,Eliq_just_NOW_string.split(",")[2])
    
    Eliq_list.sort()
    
    Eliq_array_0 = str (Eliq_list[0])
    if Eliq_array_0[2:11] == 'channelid':
        pass
    
    if Eliq_array_0[2:7] == 'power':
        print ( Eliq_array_0[2:7] )
        print ( Eliq_array_0[9:14] )
        power_value = Eliq_array_0[9:14]
        power_value_int = int (float (power_value))
    if Eliq_array_0[2:13] == 'createddate':
        pass
        
    Eliq_array_1 = str (Eliq_list[1])
    if Eliq_array_1[2:11] == 'channelid':
        pass
    
    if Eliq_array_1[2:7] == 'power':
        print ( Eliq_array_1[2:7] )
        print ( Eliq_array_1[9:14] )
        power_value = Eliq_array_1[9:14]
        power_value_int = int (float (power_value))
    
    if Eliq_array_1[2:13] == 'createddate':
        pass
        
    Eliq_array_2 = str (Eliq_list[2])
    if Eliq_array_2[2:11] == 'channelid':
        pass
    
    if Eliq_array_2[2:7] == 'power':
        print ( Eliq_array_2[2:7] )
        print ( Eliq_array_2[9:14] )
        power_value = Eliq_array_2[9:14]
        power_value_int = int (float (power_value))
    
    if Eliq_array_2[2:13] == 'createddate':
        pass
    
    if power_value_int >= 2000:
        speak.Speak(power_value)
        speak.Speak ("Warning!")
    else:
        speak.Speak(power_value)
        speak.Speak ("Good!")
        
    time.sleep(10)
    
