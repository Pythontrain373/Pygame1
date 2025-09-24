from tkinter import *
from datetime import date
from tkinter import messagebox
root = Tk()
root.title('Age Calculator App')
root.geometry('400x400')
lb1 = Label(root, text="Name", bg="#3895D3", fg='white', width=12)
lb2 = Label(root, text="Date", bg="#3895D3", fg='white', width=12)
lb3 = Label(root, text="Month", bg="#3895D3", fg='white', width=12)
lb4 = Label(root, text="Year", bg="#3895D3", fg='white', width=12)
name_entry = Entry(root)
date_entry = Entry(root)
month_entry = Entry(root)
year_entry = Entry(root)
textbox = Text(root, bg="#BEBEBE", fg="black", height=5, width=40)
def calculate_age():
    try:
        day = int(date_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        birth_date = date(year, month, day)
        today = date.today()
        age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
        textbox.delete('1.0', END)
        textbox.insert('1.0', f"Hello, {name_entry.get()}.\nYou are {age} years old.")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for date, month, and year.")
    except Exception as e:
        messagebox.showerror("An error occurred", str(e))
btn = Button(root, text="Calculate Age", command=calculate_age, bg="red")
lb1.place(x=10, y=20)
name_entry.place(x=140, y=20)
lb2.place(x=10, y=80)
date_entry.place(x=140, y=80)
lb3.place(x=10, y=110)
month_entry.place(x=140, y=110)
lb4.place(x=10, y=140)
year_entry.place(x=140, y=140)
btn.place(x=130, y=210)
textbox.place(x=10, y=250)
root.mainloop()
#I had to use google for the define part so can you teach that to me in the next lesson