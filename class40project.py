from tkinter import *
root=Tk()
def convert():
    inches=float(entry.get())
    cm=inches*2.54
    result.config(text=str(cm)+" cm")
root.geometry("400x400")
root.title("Length Converter App")
entry=Entry(root)
entry.pack()
button=Button(root,text="Convert",command=convert)
button.pack()
result=Label(root,text="")
result.pack()
root.mainloop()