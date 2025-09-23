"""Number Pad
Outline:
Create a root window that contains a number pad similar to a phone dialer using the Python Tkinter library
from tkinter import *
root=Tk()
root.title('Number Pad')
root.geometry('250x300')
nums=[[9,8,7],[6,5,4],[3,2,1],['#',0,'*']]
for i in range(4):
    root.columnconfigure(i,weight=1,minsize=75)
    root.rowconfigure(i,weight=1,minsize=50)
for i in range(4):
    for j in range(3):
        frame=Frame(master=root,relief=SUNKEN,borderwidth=1,bg="#d0efff")
        frame.grid(row=i,column=j,sticky="nsew")
        label=Label(master=frame,text=nums[i][j],bg='#d0efff',font=('Arial',18))
        label.pack(expand=True,fill='both',padx=5,pady=5)
root.mainloop()"""



"""Login App
Outline:
Write a program using the Tkinter library to create a Login Application for users."""
from tkinter import *
root=Tk()
root.title('Login App')
root.geometry('400x400')
frame=Frame(master=root, height=200, width=360,bg="#d0efff")
lb1=Label(frame,text="Full Name",bg="#3895D3",fg='white',width=12)
lb2=Label(frame,text="Email Id",bg="#3895D3",fg='white',width=12)
lb3=Label(frame,text="Enter Password",bg="#3895D3",fg='white',width=12)
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")
def display():
    name=name_entry.get()
    greet="Hey "+name
    message="\nCongratulations for your new account!"
    textbox.insert(END,greet)
    textbox.insert(END,message)
textbox=Text(bg="#BEBEBE",fg="black")
btn=Button(text="Create Account",command=display,bg="red")
frame.place(x=20,y=0)
lb1.place(x=20,y=20)
name_entry.place(x=150,y=20)
lb2.place(x=20,y=80)
email_entry.place(x=150,y=80)
lb3.place(x=20,y=140)
pass_entry.place(x=150,y=140)
btn.place(x=130, y=210)
textbox.place(y=250)
root.mainloop()