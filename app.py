import tkinter as tk
import random
from tkinter import *
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=500, height=400)
canvas.grid(columnspan=3, rowspan=3)


#logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

#instructions

instructions = tk.Label(root, text="click below to check your house", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1) 

#entry
e= Entry (root, width=15, font=('helvetica', 30))
e.pack
e.grid(column=1, row=1)


def name():
 hello= "hello" +" "+ e.get() +", \n"+ "welcome to the Sorting Ceremony"
 myLabel= Label(root, text="hello")
 myLabel.pack

 #text box
 text_boxq = tk.Text(root, height=5, width=40, font=('helvetica', 15))
 text_boxq.insert(1.0, hello)
 text_boxq.tag_configure("center", justify="center")
 text_boxq.tag_add("center", 1.0, "end")
 text_boxq.grid(column=1, row=3)
 browse_text.set("Name Enetred")





def house():

 mylist = ["Griffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
 perk = random.choice(mylist)
 decision= e.get() +" "+ "has been sorted into"+", \n"
 browse_text.set("Enter your Name")

 #text box
 text_box = tk.Text(root, height=5, width=30, font=('helvetica', 15))
 text_box.insert(1.0, decision + perk)
 text_box.tag_configure("center", justify="center")
 text_box.tag_add("center", 1.0, "end")
 text_box.grid(column=3, row=2)



#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:house(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15, border=20)
browse_text.set("Sort")

browse_btn.grid(column=1, row=4)



#name button
browse_text = tk.StringVar()
name_btn = tk.Button(root, textvariable=browse_text, command=lambda:name(), font="Raleway", bg="#20bebe", fg="white", height=2, width=15, border=20)
browse_text.set("Enter your Name")
name_btn.grid(column=1, row=2)




canvas = tk.Canvas(root, width=100, height=30)
canvas.grid(columnspan=3)

root.mainloop()