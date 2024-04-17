import tkinter as tk
from tkinter import ttk

def add_to_display(value):
    current = display_var.get()
    display_var.set(current + value)

def calculate():
    expression = display_var.get()
    try:
        result = eval(expression)
        display_var.set(result)
    except Exception as e:
        display_var.set("Error!")

def clear_display():
    display_var.set("")


#Main window
root = tk.Tk()
root.title("JJ's Calculator")
style = ttk.Style()
style.theme_use('vista')

#Variable to value displayed on the calculator
display_var = tk.StringVar()

#Entry widget, this displays the calculator value
display_entry = tk.Entry(root, textvariable=display_var, font=('MS Sans Serif', 14), justify='right')
display_entry.grid (row=0, column=0, columnspan=4, sticky='ew', padx=5, pady=5)

#Buttons to display - I stored it in a list
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        button = ttk.Button(root, text=text, command=lambda value=text: calculate())
    else:
        button = ttk.Button(root, text=text, command=lambda value=text: add_to_display(value))
    button.grid(row=row, column=col, padx=5, pady=5)

#Clear button
clear_button = ttk.Button(root, text='C', command=clear_display)
clear_button.grid(row=5, column=0, padx=5, pady=5, columnspan=2, sticky='ew')

#Exit button
exit_button = ttk.Button(root, text='Exit', command=root.destroy)
exit_button.grid(row=5, column=2, padx=5, pady=5, columnspan=2, sticky='ew')

#Run the tkinter event loop
root.mainloop()