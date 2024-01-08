import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import datetime
import wolframalpha
import os
import sys
import tkinter
engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('L47KRX-J2X67V5A79')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('SAARA : ' + audio)
    engine.say(audio)
    engine.runAndWait()




def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()


speak('Hello Sir, I am your digital assistant saara!')
speak('I am at your service at anytime')
speak('your order is my passinate duty')
speak('how can i help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       



        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')
        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')
        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')
        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif 'open song' in query:
            speak('okay')
            webbrowser.open('www.gaana.com')    
        elif 'open news' in query:
            speak('okay')
            webbrowser.open('www.indiatoday.in')
        elif 'open movie' in query:
            speak('okay')
            webbrowser.open_new('www.netflix.com')    
        elif 'open data camp' in query:
            speak('okay')
            webbrowser.open_new_tab('www.datacamp.co.in')
        elif ' show some images' in query:
            speak('okay')
            codepath='C:\\Users\\acer\\Desktop\\img1.jpg'
            os.starfile(codepath)
        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()
            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("nishitbohra2002@gmail.com", '9442385808')
                    server.sendmail('', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')
                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')
        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'hello' in query:
            speak('Hello Sir')
        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
        elif 'open python' in query:
            codePath =  'C:\\Users\\acer\\AppData\\Local\\Programs\\Python\\Python37-32\\python.exe'
            os.startfile(codePath)    
        elif 'open security' in query:
            codePath ='C:\\Program Files (x86)\\360\\Total Security'
            os.startfile(codePath)        
        elif 'play music' in query:
            codePath ='D:\\App\\audio\\Aira_Gaira.mp3'
            os.startfile(codePath)        
        elif 'open virtualbox' in query:
            codePath ='C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe'
            os.startfile(codePath)        

        elif 'open notes' in query:
            codePath ='C:\\Program Files\\Notepad++\\notepad++.exe'
            os.startfile(codePath)        

        elif 'want to relax' in query:
            codePath ='C:\\Users\\acer\\Desktop\\personal videos\\sufi rhymes.mp4'
            os.startfile(codePath)        
        elif 'telltime' in query:
            codepath='C:\\Program Files\\Atomic Alarm Clock\\AtomicAlarmClock.exe'
            os.startfile(codepath)
        elif 'open calculator' in query:
             codepath='Cccc:\\Windows\\System32\\calc.exe'
             os.startfile(codepath)
        elif 'open calender' in query:
             codepath='C:\\Windows\\System32'
             os.startfile(codepath)
        elif 'convert units' in query:
            root=Tkinter()
            root.geometry("400x400+250+250")
            root.title("Currency converter")
            heading= Label(root, text="Welcome to currency converter",font=('arial 13 bold'),fg="steelblue").pack()
            enteramount=Label(root, text="Enter amount ",font=('arial 20 bold')).place(x=10,y=50)
            my_num=IntVar()
            ent_box= Entry(root,width=50,textvariable=my_num).place(x=10,y=90)
            def converter():
                here=my_num.get()
                final=here*71.2
                lab=Label(root,text=("$"+str(final)),font=("arial, 25 bold"),fg="red").place(x=10,y=200)

            def reverse():
                here=my_num.get()
                final=here/71.2
                lab=Label(root,text=("$"+str(final)),font=("arial, 25 bold"),fg="green").place(x=100,y=240)
            btn1= Button(root, text="Convert",width=12,height=2,bg="lightgreen",command=converter).place(x=10,y=130)
            btn1= Button(root, text="Reverse",width=12,height=2,bg="lightgreen",command=reverse).place(x=10,y=130)
            root.mainloop()
        elif 'play some game' in query:
            from tkinter import *
            from tkinter import messagebox
            window=Tk()

            window.title("Welcome to The Gaming world TIC-Tac-Toe ")
            window.geometry("400x300")

            lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
            lbl.grid(row=0,column=0)
            lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
            lbl.grid(row=1,column=0)
            lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
            lbl.grid(row=2,column=0)

            turn=1; #For first person turn.

            def clicked1():
                global turn
                if btn1["text"]==" ":   #For getting the text of a button
                    if turn==1:
                       turn =2;
                       btn1["text"]="X"



                    elif turn==2:
                       turn=1;
                       btn1["text"]="O"
                       check();
            def clicked2():
                global turn
                if btn2["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn2["text"]="X"
                   elif turn==2:
                        turn=1;
                        btn2["text"]="O"
                        check();
            def clicked3():
                global turn
                if btn3["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn3["text"]="X"
                   elif turn==2:
                        turn=1;
                        btn3["text"]="O"
                        check();



            def clicked4():
                global turn
                if btn4["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn4["text"]="X"
                   elif turn==2:
                        turn=1;
                        btn4["text"]="O"
                        check();
            def clicked5():
                global turn
                if btn5["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn5["text"]="X"
                   elif turn==2:
                        turn=1;
                        btn5["text"]="O"
                        check();
            def clicked6():
                global turn
                if btn6["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn6["text"]="X"
                   elif turn==2:
                       turn=1;
                       btn6["text"]="O"
                       check();
            def clicked7():
                global turn
                if btn7["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn7["text"]="X"
                   elif turn==2:
                        turn=1;
                        btn7["text"]="O"
                        check();
            def clicked8():
                global turn
                if btn8["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn8["text"]="X"
                   elif turn==2:
                        turn=1;



                        btn8["text"]="O"
                        check();
            def clicked9():
                global turn
                if btn9["text"]==" ":
                   if turn==1:
                      turn =2;
                      btn9["text"]="X"
                   elif turn==2:
                        turn=1;
                        btn9["text"]="O"
                        check();
            flag=1;
            def check():
                global flag;
                b1 = btn1["text"];
                b2 = btn2["text"];
                b3 = btn3["text"];
                b4 = btn4["text"];
                b5 = btn5["text"];
                b6 = btn6["text"];
                b7 = btn7["text"];
                b8 = btn8["text"];
                b9 = btn9["text"];



                flag=flag+1;
                if b1==b2 and b1==b3 and b1=="O" or b1==b2 and b1==b3 and b1=="X":
                    win(btn1["text"])
                if b4==b5 and b4==b6 and b4=="O" or b4==b5 and b4==b6 and b4=="X":
                    win(btn4["text"]);
                if b7==b8 and b7==b9 and b7=="O" or b7==b8 and b7==b9 and b7=="X":
                    win(btn7["text"]);
                if b1==b4 and b1==b7 and b1=="O" or b1==b4 and b1==b7 and b1=="X":
                    win(btn1["text"]);
                if b2==b5 and b2==b8 and b2=="O" or b2==b5 and b2==b8 and b2=="X":
                    win(btn2["text"]);
                if b3==b6 and b3==b9 and b3=="O" or b3==b6 and b3==b9 and b3=="X":
                    win(btn3["text"]);
                if b1==b5 and b1==b9 and b1=="O" or b1==b5 and b1==b9 and b1=="X":
                    win(btn1["text"]);
                if b7==b5 and b7==b3 and b7=="O" or b7==b5 and b7==b3 and b7=="X":
                    win(btn7["text"]);
                if flag ==10:
                   messagebox.showinfo("Tie", "Match Tied!!!  Try again :)")
                   window.destroy()

            def win(player):
                ans = "Game complete " +player + " wins ";
                messagebox.showinfo("Congratulations", ans)



                window.destroy()  # is used to close the program

            btn1 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked1)
            btn1.grid(column=1, row=1)
            btn2 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked2)
            btn2.grid(column=2, row=1)
            btn3 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked3)
            btn3.grid(column=3, row=1)
            btn4 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked4)
            btn4.grid(column=1, row=2)
            btn5 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked5)
            btn5.grid(column=2, row=2)
            btn6 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked6)
            btn6.grid(column=3, row=2)
            btn7 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked7)
            btn7.grid(column=1, row=3)
            btn8 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked8)
            btn8.grid(column=2, row=3)
            btn9 = Button(window, text=" ",bg="yellow", fg="Black",width=3,height=1,font=('Helvetica','20'),command=clicked9)
            btn9.grid(column=3, row=3)

            window.mainloop()
            
        
        
