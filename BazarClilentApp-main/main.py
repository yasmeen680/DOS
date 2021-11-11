import argparse

import os
import sys
from typing import Type
from flask.json import jsonify
import requests
import json
from datetime import datetime
import urllib
import urllib3
urllib.request
import http

d = "\n-----------------------------------------------\n" 
i = "info"
p = "purchase"
ad = "/admin"
ex = "/exit"
h = "/help"
s = "search"
cp = "/change_price"

def searchcatagory(topic):
    req = requests.get('http://10.0.2.14:6060/search/{}'.format(topic))#Return a formatted version of S, using substitutions from args and kwargs
    return req.text
    

def purchaseId(id, name):
    req = requests.post('http://10.0.2.14:6060/purchase/{}'.format(id), json=({"name": name }))
    return req.text

def infoId(id):
    req = requests.get('http://10.0.2.14:6060/info/{}'.format(id))
    return req.text
   
    print("\n Welcome  \n")
    
commandslist = ["s {title}", "i {item}", "p {item}"]

Userinput = ""
while (True) :
    Userinput = input("> ")
    command = Userinput.split(" ",1) #Return a list of the words in the string
    if Userinput == ex :
        break
    elif Userinput == help :
        for x in commandslist :
            print("  # "+x+"\n")
    elif len(command) < 2 :
        print("  invalid command")
    else :
        if command[0] == s:
            print(searchcatagory(command[1]))

        elif (command[0] == i) :
            print(infoId(command[1]))

        elif (command[0] == p) :
            print("Enter the name: ")
            clientName = input("< ")
            print("  " + purchaseId(command[1], clientName))

        else :
            print("  invalid ")



