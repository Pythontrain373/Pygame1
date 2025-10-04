from tkinter import *
root=Tk()
root.geometry("400x400")
root.title("Length Converter App")
entry=Entry(root)
entry.pack()
label=Label(root,text="",font=("Arial",14))
label.pack()
def checkstrength():
    len=len(entry.get())
    if len<=5:
        label.config(text="Weak",fg="#FF0000")
    elif 6<=len<=8:
        label.config(text="Medium",fg="#FFFF00")
    elif 9<=len<=12:
        label.config(text="Strong",fg="#90EE90")
    else:
        label.config(text="Very Strong",fg="#006400")
btn=Button(root,text="Check Strength",command=checkstrength,bg="#ADD8E6")
btn.pack()
root.mainloop()