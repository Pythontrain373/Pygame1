import tkinter as tk
import random
root=tk.Tk()
root.title("Rock Paper sissor")
root.geometry("400x400")
def checkwinner(userchoice):
    computerchoice=random.choice(['rock','paper','scissors'])
    if userchoice==computerchoice:
        result="It's a tie!"
    elif(userchoice=='rock'and computerchoice=='scissors')or(userchoice=='paper'and computerchoice=='rock')or(userchoice=='scissors'and computerchoice=='paper'):
        result="You win!"
    else:
        result="Computer wins!"
    resultlabel.config(text=f"Computer chose: {computerchoice}\n{result}")
rockbutton=tk.Button(root,text="Rock",command=lambda:checkwinner('rock'))
rockbutton.pack(pady=10)
paperbutton=tk.Button(root,text="Paper",command=lambda:checkwinner('paper'))
paperbutton.pack(pady=10)
scissorsbutton=tk.Button(root,text="Scissors",command=lambda:checkwinner('scissors'))
scissorsbutton.pack(pady=10)
resultlabel=tk.Label(root,text="")
resultlabel.pack(pady=20)
root.mainloop()