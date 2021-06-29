import speech_recognition as sr
import pyttsx3
from tkinter import *
from gtts import gTTS
import os
import sys
from textblob import TextBlob

myText0 = "welcome to The Analyzer. kindly click on the give review button to continue."
language = 'en'
output = gTTS(text=myText0,lang=language,slow=False)
output.save("start0.wav")

myText = "please start speaking"
language = 'en'
output = gTTS(text=myText,lang=language,slow=False)
output.save("start1.wav")

myText2 = "Your review has been saved. Performing sentiment analysis. Thankyou for your review."
language = 'en'
output = gTTS(text=myText2,lang=language,slow=False)
output.save("start2.wav")

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

root = Tk()

Label01 = Label(root, text="Welcome To The Analyzer\n\n")
Label01.pack()
Label02 = Label(root, text="Instructions : \n")
Label02.pack()
Label03 = Label(root, text="1. Click on the \"Give Review\" Button and wait for the program to speak to you.")
Label03.pack()
Label69 = Label(root, text="2. To give a review with more than one sentences, add an \"and\" between the sentences.\n\n")
Label69.pack()
os.system("start start0.wav")

r = sr.Recognizer()

def sentianalysis():
    Label04 = Label(root,text="\n\nDATA : \n\n\n").pack()

    pos_count=0
    pos_correct=0
    neg_count=0
    neg_correct=0
   
    with open("latest.txt","r") as f:

        for line in f.read().split('and'):

            analysis=TextBlob(line)
           
            if(analysis.sentiment.polarity>=0.5):
                if analysis.sentiment.polarity>0.1:
                    pos_correct += 1
                    Label902 = Label(root, text=line+" - Positive sentiment Detected").pack()

                pos_count += 1
                
            elif(analysis.sentiment.polarity<0):
                if analysis.sentiment.polarity<0:
                    neg_correct += 1
                    Label900 = Label(root, text=line+" - Negative Sentiment Detected").pack()

                neg_count += 1

            if(analysis.sentiment.polarity==0):
                if analysis.sentiment.polarity==0:
                    Label901 = Label(root, text=line + " - Neutral Sentiment Detected").pack()

def speechrecrd():
    try:
        with sr.Microphone() as source2:

            r.adjust_for_ambient_noise(source2, duration=0.2)

            os.system("start start1.wav")
            
            audio2 = r.listen(source2)

            speech = r.recognize_google(audio2)

            db = open("database.txt","a")
            ls = open("latest.txt","w")

            db.write(speech)
            db.write("\n")
            ls.write(speech)

            db.close()
            ls.close()

            Label05 = Label(root,text="---------------------------------------------------------------------------\n\nYour Review : ")
            Label05.pack()

            Label06 = Label(root,text=speech)
            Label06.pack()

            os.system("start start2.wav")

            sentianalysis()

            Label07 = Label(root, text="\n\nThank you.\n\n---------------------------------------------------------------------------")
            Label07.pack()

            restart_btn = Button(root, text="Give Another Review", command=restart_program)
            restart_btn.pack()
            exit_btn = Button(root, text="Exit", command=root.quit)
            exit_btn.pack()
    except:
        Label100 = Label(root, text="An Error has occured!").pack()
        Label101 = Label(root, text="Please check your Internet Connetion.").pack()
        Label103 = Label(root, text="Otherwise, click on the restart button below to restart the program.").pack()
        restart_btn02 = Button(root, text="Restart", command=restart_program).pack()
        
record_btn = Button(root, text="Give Review", command=speechrecrd)
record_btn.pack()

root.mainloop()
