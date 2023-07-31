from tkinter import *
from time import *

def update():
    time_string = strftime("%I:%M:%S %p")
    time_label.config(text=time_string)

    day_string = strftime("%A")
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")
    date_label.config(text=date_string)

    window.after(1000, update)


window = Tk()
window.title("時計")

photo = PhotoImage(file="clockimge.png")
window.iconphoto(True, photo)

time_label = Label(window, font=("Arial", 50), fg="pink", bg="black")
time_label.pack()

day_label = Label(window, font=("Cambria", 40), fg="hotpink")
day_label.pack()

date_label = Label(window, font=("Cambria", 35), fg="hotpink")
date_label.pack()

update()

window.mainloop()



