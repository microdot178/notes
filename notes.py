# !/usr/bin/python3
# coding=utf-8
from tkinter import *
#import pickle
from ewmh import EWMH
import tkinter as tk
import json

#название файла, откуда буду брать текст заметок и туда же буду его сохранять
#notesdata = 'notes.data'
#placedata = 'place.data'

#загружаю текст из файла notesdata
#f=open(notesdata, 'rb')
#storedtext = pickle.load(f)

#f=open(placedata, 'rb')
#coordinates = pickle.load(f)

with open('sw_templates.json') as f: # теперь сохраняться и загружаться будет в json
    data = json.load(f)

notestext = data['notestext']
coordinates = data['coordinates']

#создаю функцию, которая захватывает текст и сохраняет его в notes.data
def SaveText():
    s = text.get(1.0, END)
    label['text'] = s
    notestext = s
    #f=open(notesdata, 'wb')
    #pickle.dump(notestext, f)
    coordinates = root.geometry()
    #f=open(placedata, 'wb')
    #pickle.dump(coordinates, f)
    #f.close()
    data = {'coordinates': coordinates, 'notestext': notestext} # json 
    with open('sw_templates.json', 'w') as f:                   # json
        f.write(json.dumps(data))                               # json


#создаю событие, которое будет выполнять функцию SaveText, при нажатии CTRL+S
def CtrlS(event):
    root.after(10, ctrl_s, event.widget)

def ctrl_s(widget):
    SaveText()

#создаю событие, которое будет выполнять SaveText, при закрытии программы
def on_closing():
    SaveText()
    root.destroy()

#!!
ewmh = EWMH()

#создаю окно приложения
root = tk.Tk()
root.title("")
root.geometry(coordinates)

root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file='favicon.png'))
root.lift()
#root.wm_attributes("-alpha", 0.8)



#один из способов установить свою иконку, не работает бля!
#root.iconbitmap('favicon/favicon.gif')

#!!
root.update_idletasks()     # to make sure the window is displayed
w = ewmh.getActiveWindow()  # get the window
ewmh.setWmState(w, 1, '_NET_WM_STATE_SKIP_TASKBAR')  # remove window from taskbar
ewmh.display.flush()

#временное решение против сворачивания крови и окна
#root.bind('<Unmap>', lambda event: event.widget.deiconify())

text = Text(width=40, height=40, font='Arial 11')
text.pack()

frame = Frame()
frame.pack()


area=notestext

label = Label()
label.pack()


text.insert(1.0, area)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.bind('<Control-s>',ctrl_s)
root.mainloop()
