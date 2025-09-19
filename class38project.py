from tkinter import *
root=Tk()
root.geometry('400x300')
def calculate_product():
    a=int(entry1.get())
    b=int(entry2.get())
    product=a*b
    result_label.config(text=f'Product: {product}')
root.title('Product Calculator')
entry1=Entry(root)
entry1.pack()
entry2=Entry(root)
entry2.pack()
calculate_button=Button(root,text='Calculate',command=calculate_product)
calculate_button.pack()
result_label=Label(root,text='')
result_label.pack()
root.mainloop()