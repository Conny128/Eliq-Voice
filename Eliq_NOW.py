import requests
import json
import time


Eliq_list = []
b=0
a=0
length = 0
power_index=0

response = requests.get ("https://my.eliq.io/api/datanow?accesstoken=745109ac4bed4c318ff47b06e5285f95&channelid=32217")

Eliq_just_NOW_string = str (response.json())
#print (Eliq_just_NOW_string)
Eliq_list.insert(0,Eliq_just_NOW_string.split(",")[0])
Eliq_list.insert(1,Eliq_just_NOW_string.split(",")[1])
Eliq_list.insert(2,Eliq_just_NOW_string.split(",")[2])

Eliq_list.sort()

Eliq_array_0 = str (Eliq_list[0])
if Eliq_array_0[2:11] == 'channelid':
    pass
    #print ('CHANNELID')
    #print ( Eliq_array_0[2:11] )
if Eliq_array_0[2:7] == 'power':
    print ( Eliq_array_0[2:7] )
    print ( Eliq_array_0[9:14] )
if Eliq_array_0[2:13] == 'createddate':
    pass
    #print ('CREATEDATE')
    #print ( Eliq_array_0[2:13] )
    
Eliq_array_1 = str (Eliq_list[1])
if Eliq_array_1[2:11] == 'channelid':
    pass
    #print ('CHANNELID')
    #print ( Eliq_array_1[2:11] )
if Eliq_array_1[2:7] == 'power':
    print ( Eliq_array_1[2:7] )
    print ( Eliq_array_1[9:14] )
if Eliq_array_1[2:13] == 'createddate':
    pass
    #print ('CREATEDATE')


    #print ( Eliq_array_1[2:13] )
    
Eliq_array_2 = str (Eliq_list[2])
if Eliq_array_2[2:11] == 'channelid':
    pass
    #print ('CHANNELID')
    #print ( Eliq_array_2[2:11] )
if Eliq_array_2[2:7] == 'power':
    print ( Eliq_array_2[2:7] )
    print ( Eliq_array_2[9:14] )
if Eliq_array_2[2:13] == 'createddate':
    pass
    #print ('CREATEDATE')
    #print ( Eliq_array_2[2:13] )


