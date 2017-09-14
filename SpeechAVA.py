#Importing the Pyttsx3 module for text to speech conversion
import pyttsx3

#Function to convert text to speech passed as value
def speech(text):
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate-20)
    engine.say(text)
    engine.runAndWait()
'''text='enter'
   while text!='exit':
   speech(text)
   text = str(input('Enter the text: '))'''
