from tkinter import *
import tkinter as tk
from tkinter import ttk
import modul_TTS

window=Tk()
root = tk.Tk()

label = ttk.Label(root)
label["text"] = "Velkommen"
label.pack()

def button_clicked():
    print("button clicked") #kommer ut i kommandlinjen
    modul_TTS.speak("You pressed the button")

button = ttk.Button(root, text="click me",command=button_clicked)
button.pack()

def return_pressed(event):
    print("return key pressed")

def log(event):
    print(event)

root = tk.Tk()

btn = ttk.Button(root, text="save")
btn.bind("<Return>", return_pressed)
btn.bind("<Return>", log, add="+")

btn.focus()
btn.pack(expand=True)


root.mainloop()
#window=Tk()
#btn=Button(window, text="Save", fg='blue')
#btn.place(x=80, y=100)
#lbl=Label(window, text="Welcome to the game, please enter your name", fg='red', font=("Helvetica", 16))
#lbl.place(x=30, y=50)
#txtfld=Entry(window, text="This is Entry Widget", bd=5)
#txtfld.place(x=80, y=70)
#window.title('Hello Python')
#window.geometry("600x200+10+10")
#window.mainloop()