"""
Program: first_gui.py
Author: Andy Volesky
Last date modified: 10/27/2021
The purpose of this program:

Make a GUI that follows these specifications:
Title "Favorite Meal"
Checkbuttons: "Breakfast", "Second Breakfast", "Lunch", "Dinner" in rows 1-4 of grid
Label "Waiting" in row 5 of grid
Button "Exit" that exits in row 6 of grid
Add a Trigger event when a Checkbutton is checked.

"""

import tkinter

def pick_breakfast():
    label.config(text="The most importantest meal")

def pick_second_breakfast():
    label.config(text="The second most importantest meal")

def pick_lunch():
    label.config(text="Better go easy or you will need a nap at 1pm")

def pick_dinner():
    label.config(text="Make a good choice and try a salad.")

m = tkinter.Tk()
m.title('Favorite Meal')

label = tkinter.Label(m, text="Waiting")
label.grid(row=5)

var1 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=1)

var2 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=2)

var3 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=3)

var4 = tkinter.IntVar()
check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=4)

exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
exit_button.grid(row=6)

m.mainloop()
