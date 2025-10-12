import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(600,600)
fonttype='normal','bold','italic'
align='left','center','right'
hi=turtle.Turtle()
hi.speed(500)
import tkinter as tk
import random
root=tk.Tk()
root.title("Rock Paper sissor")
root.geometry("400x400")
def checkwinner(userchoice):
    computerchoice=random.choice(['rock','paper','scissors'])
    if userchoice==computerchoice:
        hi.clear()
        hi.write("It is a tie",font=('Courier',30,'italic'))
    elif (userchoice=='rock'and computerchoice=='scissors')or(userchoice=='paper'and computerchoice=='rock')or(userchoice=='scissors'and computerchoice=='paper'):
        hi.clear()
        hi.write("You win",font=('Courier',30,'italic'))
    else:
        hi.clear()
        hi.write("Computer wins",font=('Courier',30,'italic'))
    resultlabel.config(text=f"Computer chose: {computerchoice}")
rockbutton=tk.Button(root,text="Rock",command=lambda:checkwinner('rock'))
rockbutton.pack(pady=10)
paperbutton=tk.Button(root,text="Paper",command=lambda:checkwinner('paper'))
paperbutton.pack(pady=10)
scissorsbutton=tk.Button(root,text="Scissors",command=lambda:checkwinner('scissors'))
scissorsbutton.pack(pady=10)
resultlabel=tk.Label(root,text="")
resultlabel.pack(pady=20)
turtle.done()
root.mainloop()
