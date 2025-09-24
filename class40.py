"""Event Handler
Outline:
Write a program to handle the events of Keypress and 
Button click using the Python library Tkinter.from tkinter import *
window=Tk()
window.title("Event Handler")
window.geometry("300x300")
def handle_keypress(event):
    print(event.char)
window.bind("<Key>",handle_keypress)
def handle_click(event):
    print("\nThe button was clicked!")
button=Button(text="Click me!")
button.pack()
button.bind("<Button-1>",handle_click)
window.mainloop()"""

"""Virus Detected
Outline:
Create a Tkinter Application which consists of a root window with a button (with text Scan for the virus). When this button is clicked, it will generate a message box 
that shows a warning: Stop! Virus Found."""
from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Alert","Stop! Virus Forund.")
button=Button(root,text="Scan for Virus",command=msg)
button.place(x=40,y=80)
root.mainloop()