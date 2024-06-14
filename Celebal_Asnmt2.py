import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN
import math


window = tk.Tk()
window.title('GUI Calculator')
frame = tk.Frame(master=window, bg="skyblue", padx=10)
frame.pack()


entry = tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=4, ipady=2, pady=2)


def myclick(number):
    entry.insert(tk.END, number)


def equal():
    try:
        
        expression = entry.get().replace('^', '**')
        y = str(eval(expression))
        entry.delete(0, tk.END)
        entry.insert(0, y)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", f"Syntax Error: {e}")


def clear():
    entry.delete(0, tk.END)


def sqrt():
    try:
        number = float(entry.get())
        result = math.sqrt(number)
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", f"Syntax Error: {e}")


def power():
    entry.insert(tk.END, '**')


def percent():
    try:
        number = float(entry.get())
        result = number / 100
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except Exception as e:
        tkinter.messagebox.showinfo("Error", f"Syntax Error: {e}")


buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('0', 4, 1), ('/', 4, 3), ('%', 4, 0), ('sqrt', 4, 2),
    ('clear', 5, 0, 2), ('=', 5, 2, 2), ('^', 6, 0)
]


for (text, row, col, *colspan) in buttons:
    if text == '=':
        action = equal
    elif text == 'clear':
        action = clear
    elif text == 'sqrt':
        action = sqrt
    elif text == '^':
        action = power
    elif text == '%':
        action = percent
    else:
        action = lambda x=text: myclick(x)

    
    columnspan = colspan[0] if colspan else 1

    button = tk.Button(master=frame, text=text, padx=15, pady=5, width=3, command=action)
    button.grid(row=row, column=col, columnspan=columnspan, pady=2)


def key_event(event):
    key = event.char
    if key in '0123456789+-*/.':
        myclick(key)
    elif key == '\r':  
        equal()
    elif key == '\x08':  
        entry.delete(len(entry.get())-1, tk.END)

window.bind('<Key>', key_event)


window.mainloop()
