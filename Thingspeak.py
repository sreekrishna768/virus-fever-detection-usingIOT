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
    
if __name__ == '__main__':
    thingspeak_post()
