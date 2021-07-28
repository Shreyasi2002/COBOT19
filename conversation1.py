import os
import aiml
from flask import Flask, redirect
from autocorrect import spell
import webbrowser

app = Flask(__name__)
k = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    k.bootstrap(brainFile = "bot_brain.brn")
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="learningFileList.xml",commands="Load conversation")
    #k.saveBrain("bot_brain.brn") 


I = input(">>>>> ")
while I != "QUIT" :
    print(k.respond(I)) 
    d= k.getPredicate('date')
    if I== "3"  :
        webbrowser.open("https://www.worldometers.info/coronavirus/country/india/") 
    elif I== "15" :
        webbrowser.open("https://www.bharatbiotech.com/covaxin.html")   
    elif I== "19" :
        webbrowser.open("https://www.google.com/maps/place/"+d)   
    elif I== "25" :
        webbrowser.open("https://youtu.be/UE_H9QhGktE")  
    elif I=="26" :
        webbrowser.open("https://youtu.be/UcFDdfueQRg")                
    I = input(">>>>> ")