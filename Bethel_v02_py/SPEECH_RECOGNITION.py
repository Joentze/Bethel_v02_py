#!/usr/bin/env python

#IMPORTS SPEECH RECOGNITION LIBRARY
import speech_recognition as sr

#import SPEECH as sp 

#IMPORTS BEST MATCHED MODULE
import BEST_MATCHED as Bm

#IMPORTS LISTED_NEST_DICT MODULE
import LIST_NESTED_DICT as dictList

#IMPORTS FUCNTION_EXEC MODULE
import FUNCTIONS_EXEC as func_exec

#IMPORTS OS MODULE
import os

r = sr.Recognizer()
mic =  sr.Microphone()

list_of_words_file = os.listdir("/" + "combinationFunctions")
print(list_of_words_file)


def inputString():
    while False:
        with mic as source:
            print('speak anything')
            audio = r.listen(source)
            sr.Microphone.list_microphone_names()
                
        try:
            
            text = r.recognize_google(audio)

            print('transript: {}'.format(text))


        except:
            print("can't hear anything")
        
    
inputString()