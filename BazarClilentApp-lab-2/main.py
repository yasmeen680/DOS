import time
import argparse

import os
import sys
from typing import Type
from flask.json import jsonify
import requests
import json
from datetime import datetime
import time
import urllib
urllib.request
import urllib3
import http 

d = "\n-----------------------------------------------\n"  # variable divider
h = "/help"     # help
s = "search"     # search
i = "info"        # info
ex = "/exit"   # exit
p = "purchase"     # purchase
cp = "/change_price"   # changeprice



#Time_info_request and response
def infobyId(id):
    timebefore = float(time.time())
    n = time.ctime(timebefore)
    print("Time_info_request: {0}".format(n))
    req = requests.get('http://localhost:4000/info/{}'.format(id))
    timeafter = float(time.time())
    now = time.ctime(timeafter)
    print("Time_info_response: {0}".format(now)) #Return a formatted version of S, using substitutions from args and kwargs
    print("Response Time: ", req.elapsed.total_seconds()) #Total seconds in the duration.
    timetaken = timeafter - timebefore
    print ("Latency: ", timetaken)
    
    return req.text


    #Time_search_response and request 
def searchBycatagory(topic):
    timebefore = float(time.time())  #module provides various functions to manipulate time values
    n = time.ctime(timebefore)    #Convert a time in seconds since the Epoch to a string in local time
    print("Time_search_request: {0}".format(n)) #Return a formatted version of S
    req = requests.get('http://localhost:4000/search/{}'.format(topic))
    timeafter = float(time.time())
    now = time.ctime(timeafter)
    print("Time_search_response: {0}".format(now))
    print("Response Time: ", req.elapsed.total_seconds()) #Response Time
    timetaken = timeafter - timebefore
    print ("Latency: ", timetaken)
    
    return req.text

#Time_purchase_request and response
def purchaseId(id, name):
    timebefore = float(time.time()) #There are two standard representations of time
    n = time.ctime(timebefore)
    print("Time_purchase_request: {0}".format(now1))
    req = requests.post(
        'http://localhost:4000/purchase/{}'.format(id), json=({"name": name}))
    timeafter = float(time.time())
    now = time.ctime(timeafter) #current time as returned by localtime() is used
    print(
        "Time_purchase_response: {0}".format(now))
    print("Response Time: ", req.elapsed.total_seconds())
    timetaken = timeafter - timebefore
    print ("Latency: ", timetaken)
    
    return req.text


commandlist = ["s {title}", "i {item}", "p {item}"]



Userinput = ""
while (True):
    Userinput = input("> ")
    command = Userinput.split(" ", 1)
    if Userinput == ex:
        break
    
    else:
        if command[0] == s:
            print(searchBycatagory(command[1]))

        elif (command[0] == i):
            print(infobyId(command[1]))

        elif (command[0] == p):
            print("Enter The name: ")
            clientName = input("< ")
            print("  " + purchaseId(command[1], clientName))

        else:
            print("  invalid ")


