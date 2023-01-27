from tkinter import *
from PIL import ImageTk,Image
import modul_TTS
from tkinter import messagebox
root = Tk()
root.title("Testprogram")

welcome = Label(root, text="Welcome to our game!").grid(row=2, column=5)
welcome1 = Label(root, text="Please enter your name:").grid(row=3, column=5)
Entry(root, width=50).grid(row=3, column=7)

my_img = ImageTk.PhotoImage(Image.open("bilde2.png"))
myLabel = Label(image=my_img)
myLabel.grid(row=2)

#def myClick():
#    hello = "Hello "+namebox.get()
#    myLabel = Label(root, text=hello)
#    modul_TTS.speak("aaaaaah")
#    myLabel.grid(row=4, column=2)

#print(namebox)

#myButton = Button(root, text="Enter your name!", command=myClick)
#myButton.grid(row=4, column=7)
exitButton = Button(root, text="exit", command=root.quit, width=25)
exitButton.grid(row=10, column=5, rowspan=3)

frame = LabelFrame(root, text="this is a frame ....", padx=5, pady=5)
frame.grid(row=10)

b = Button(frame, text="don't click here")
b.grid(row=11)

#forskjellige typer varseler # showinfo, showwarning, showerror, askquestion, askokcancel, askyesno
def popup():
    response = messagebox.askyesno("this is a pop up", "hello world")
    Label(root, text=response).grid(row=2)
    if response ==1:
        Label(root, text="You klicked yes").grid(row=2)
    if response == 2:
        Label(root, text="You klicked no").grid(row=2)

knapp = Button(frame, text="popup", command=popup).grid(row=5)


root.mainloop()

#name.Insert(0,"enter your name")


#creating a label widget
#myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
#myLabel2 = Label(root, text="My name is John Cena")
#myLabel3 = Label(root, text="My name is John Cena")
#Shoving it onto the screen
#myLabel1.pack()

#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=2)
#myLabel3.grid(row=4, column=5)

#entry = Entry(root, width=50, bg="gray", borderwidth=10)
#entry.pack()
#entry.get()
#entry.insert(0,"Enter your name: ")

#def myClick():
#    hello = "Hello "+entry.get()
#    myLabel = Label(root, text=hello)
#    modul_TTS.speak("aaaaaah")
#    myLabel.pack()

#myButton = Button(root, text="Enter your name!", command=myClick, fg="blue", bg="red")
#myButton.pack()




