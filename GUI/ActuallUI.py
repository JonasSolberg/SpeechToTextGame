from tkinter import *
from PIL import ImageTk,Image
import modul_TTS
from tkinter import messagebox
root = Tk()
root.title("The Game")
root.geometry("900x800")
#BreddeXHøyde

#tekst som sier hei
header1 = Label(root, text="Welcome to the the game")
header1.grid(row=1,column=2)

#logo for spiller
my_img = ImageTk.PhotoImage(Image.open("../bilde2.png"))
myLabel = Label(image=my_img)
myLabel.grid(row=2, column=3)

#knapp for å starte selve spillet
startButton = Button(root, text="Start", width=25)
startButton.grid(row=3, column=5)

#knapp for å avslutte
exitButton = Button(root, text="exit", command=root.quit, width=25)
exitButton.grid(row=3, column=3, rowspan=3)




root.mainloop()