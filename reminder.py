from pygame import mixer
from win10toast import ToastNotifier

import gtts
import time
import tkinter as tk
def sound():
    mixer.init()
    mixer.music.load('C:\\Users\\Om\\AppData\\Local\\Programs\\Python\\Python36-32\\txt.mp3')

def alarm():
    tts =gtts.tts.gTTS(text.get(),lang='en')
    tts.save("txt.mp3")
    n=5
    print( 'reminder set for ' + hours.get() + minutes.get() + sec.get())
    while True:
        if time.localtime().tm_hour==int(hours.get()) and time.localtime().tm_min==int(minutes.get()) and time.localtime().tm_sec==int(sec.get()):
            txt=text.get()
            print(txt)
            
            break
    sound()
    while n>0:
        toast=ToastNotifier()
        toast.show_toast("Reminder",text.get(),duration=30)
        mixer.music.play()
        time.sleep(3)
        n=n-1
    sn=str(input('press s for snooze'))
    if sn=='s':
        n=3
        time.sleep(100)
        while n>0:
            mixer.music.play()
            time.sleep(2)
    else:
        exit()



    

root=tk.Tk()
L1=tk.Label(root,text="Hours")
hours= tk.Entry(root)
L2=tk.Label(root,text="minutes")
minutes= tk.Entry(root)
L3=tk.Label(root,text="seconds")
sec= tk.Entry(root)
L4=tk.Label(root,text="Reminder Text")
text=tk.Entry(root)
b1=tk.Button(root , text="submit", font = 30, width = 10, command=alarm)
L1.grid(row=0,column=0)
hours.grid(row=0,column=1)
L2.grid(row=0,column=2)        
minutes.grid(row=0,column=3)
L3.grid(row=0,column=4)
sec.grid(row=0,column=5)
L4.grid(row=1,column=0)
text.grid(row=1,column=1)
b1.grid(row=1,column=2)
root.mainloop()
    
