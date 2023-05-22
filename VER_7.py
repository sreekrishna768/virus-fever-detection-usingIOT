# Importing Libraries
import serial
import time
import csv
#from csv import writer


import time
import datetime
import pandas as pd
import numpy as np
import Thingspeak
import urllib.request
import requests
import threading
import json

import random

def thingspeak_post():
    threading.Timer(15,thingspeak_post).start()
    val=random.randint(1,30)
    URl='https://api.thingspeak.com/update?api_key='
    KEY='5T9KE92N4SMHSO1Q'
    HEADER='&field1={}&field2={}&field3={}&field4={}&field5={}&field6={}&field7={}&field8={}'.format(str(val),str(val),str(val),str(val),str(val),str(val),str(val),str(val))
    NEW_URL = URl+KEY+HEADER
    print(NEW_URL)
    data=urllib.request.urlopen(NEW_URL)
    print(data)
    

name='VELAMMAL'

#Python sending data over the serial port.

arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)



def READ_RFDATA(x):
    #arduino.write("FS##".encode())
    #time.sleep(1)
    data = arduino.readline().decode()
    return data


#Char to integer convertion for LCD display

def split(x):
    data=[]
    SV=str(x)
    SVV = SV.split("'b'Message: A:")
    data =SVV


    return data


while True:
# intial declaration

   
    num = 1
    nus=5
   
    
    time.sleep(1)
    data=READ_RFDATA(num)

    
    Temp1=data.split(",")

    
    

##    if(len (Temp1) > 5):      
##        print(Temp1[1])
##        print(Temp1[3])
##        print(Temp1[5])
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')            
        #attendance = [name, date, timeStamp,sensor1,sensor2,sensor3]
    #sensor1=Temp1[1]
    #sensor2=Temp1[3]
    #sensor3=int(Temp1[5])
    #print(sensor3)
    data = {'Date' :date,'Time':timeStamp,'sens-1':[data],'sens-2':[data],'sens3':[str(data)],}
    print(data)
    df = pd.DataFrame(data)
    thingspeak_post()

    df.to_csv('BIO.csv', mode='a', index=False, header=False)   
                      

  
    

