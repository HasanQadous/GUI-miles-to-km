from tkinter import *

window = Tk()
window.title("Miles to KM")
window.minsize(width=300, height=300)
window.config(padx=20, pady=20)

my_label = Label(text="", font=("Ariel", 24))
my_label.grid(column=0, row=0)
miles = Label(text="Miles")
miles.grid(column=2, row=0)
km = Label(text="KM")
km.grid(column=2, row=1)
equal = Label(text="is equal to")
equal.grid(column=0, row=1)
result = Label(text="0")
result.grid(column=1, row=1)


def click_me():
    x = float(input.get())
    y = round(x*1.609)
    result.config(text=y)


button = Button(text="Calculate", command=click_me)
button.grid(column=1, row=2)

input = Entry(width=7)
input.grid(column=1, row=0)

window.mainloop()
