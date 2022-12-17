# Import modules
from tkinter import *
from PIL import Image, ImageTk

# Create object
root = Tk()

# Adjust size
root.geometry("1900x1190")

# Create Label
label1 = Label(root, text="Disease Prediction for Breast Cancer Data Set ")
label1.pack()

# Functions :
# -----------

# Change the label text
def show():
    label.config(text=clicked.get())

# saves the form in the csv format
def save_form(input1, input2):
    with open('form_data.txt', 'a') as text_file:
        text_file.write(input1 + '\n')
        text_file.write(input2 + '\n')

# model parameters function on click
def submit():
    if clicked.get() == "Neural Network":
        on_click()
    elif clicked.get() == "Random Forest":
        on_click()
    else:
        button4 = Button(root, text="Input parameters", command=on_click).pack()

def on_click():
    # Create the input fields
    input1 = Entry(root)
    input1_label = Label(root, text="Parameter 1:")
    input2 = Entry(root)
    input2_label = Label(root, text="Parameter 2:")

    input1_label.pack()
    input1.pack()
    input2_label.pack()
    input2.pack()

    # Create the Train button
    button3 = Button(root, text="Train", command=lambda: save_form(input1.get(), input2.get()))
    button3.pack()

# --------------

# Dropdown menu options
options = [
    " "
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Select a Machine Learning model")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options)
drop.pack()

# Add commands to options
drop["menu"].add_command(label="Random Forest", command=submit)
drop["menu"].add_command(label="Neural Network", command=submit)

# Create submit button, it will change label text
# button = Button( root , text = "Submit" , command = submit ).pack()

# Create Label
if clicked.get() == "Neural Network":
    label = Label(root, text="Neural Network")
    label.pack()

# Create a button with the text "Input Parameters"
# and specify the function to be called when the button is clicked
# button1 = Button(root, text="Input parameters", command= on_click ).pack()

# Execute tkinter
root.mainloop()
