from tkinter import Tk, Button, Entry, Text, END, DoubleVar, Label

window = Tk()


GRAM = 1000
POUND = 2.20462
OUNCE = 35.274


def convert_to_grams():
    grams.delete('1.0', END)
    grams.insert(END, e1_value.get() * GRAM)


def convert_to_pounds():
    pounds.delete('1.0', END)
    pounds.insert(END, e1_value.get() * POUND)


def convert_to_ounces():
    ounces.delete('1.0', END)
    ounces.insert(END, e1_value.get() * OUNCE)


def convert():
    convert_to_grams()
    convert_to_pounds()
    convert_to_ounces()


e1 = Label(window, text="Kg")
e1.grid(row=0, column=0)

b1 = Button(window, text='Convert', command=convert)
b1.grid(row=0, column=2)

e1_value = DoubleVar()
e1 = Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

grams = Text(window, height=1, width=20)
grams.grid(row=1, column=0)

pounds = Text(window, height=1, width=20)
pounds.grid(row=1, column=1)

ounces = Text(window, height=1, width=20)
ounces.grid(row=1, column=2)


window.mainloop()
