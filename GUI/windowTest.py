from tkinter import *
from PIL import ImageTk,Image

#WE DON'T NEED THIS FILE ANYOMORE

root = Tk()
root.title("tittel på side")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to=200)


def open():
    global my_img
    top = Toplevel()
    label = Label(top, text="Hello World").pack()
    my_img = ImageTk.PhotoImage(Image.open("../bilde2.png"))
    label1 = Label(top, image=my_img).pack()
    btn2 = Button (top, text="close window", command=top.destroy).pack()


knapp = Button(root, text="Open second window", command=open).pack()


#top = Toplevel()
#label = Label(top, text="Hello World").pack()
#my_img = ImageTk.PhotoImage(Image.open("bilde2.png"))
#label1 = Label(top, image=my_img).pack



mainloop()
