"""Pygame Window
Outline:
Write a Python program to - create an empty Tkinter window, set the title to it, and set its geometry.
from tkinter import *
root=Tk()
root.title('Getting Startted with widgets')
root.geometry('400x300')
root.mainloop()#always the last line"""

"""Getting started with widgets
Outline:
Write a program to create a Pygame window that takes the user's name as input and displays a personalized message. 
Use labels, buttons, entry, 
and text widgets to develop this application."""
from tkinter import *
from datetime import date
root=Tk()
root.title('Getting Startted with widgets')
root.geometry('400x300')
lbl=Label(text="Hey there", fg='red',bg="#57D9E5",height=1,width=300)
lbl.pack()
name_lbl=Label(text="Full Name",bg="#B0E6CD")
name_lbl.pack()
name_entry=Entry()
name_entry.pack()
text_box=Text(height=4)
def display():
    name=name_entry.get()
    global Message
    message="Welcome to the Application!\nToday's date is: "
    greet="Hello "+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
btn=Button(text='Begin',command=display,height=1,bg="#FEEEB4",fg='black')
btn.pack()
text_box.pack()
root.mainloop()