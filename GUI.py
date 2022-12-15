# Import modules
from tkinter import *

# Create object
root = Tk()

# Adjust size
root.geometry( "1000x1000" )




# Change the label text
def show():
	label.config( text = clicked.get() )

# saves the form in the csv format
def save_form(input1, input2):
	with open('form_data.txt', 'a') as text_file:
		text_file.write(input1 + '\n')
		text_file.write(input2 + '\n')

# model parameters function on click
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
 

    # Create the submit button
    button3 = Button(root, text="Submit", command=lambda: save_form(input1.get(), input2.get()))
    button3.pack()

    # Update the canvas and frame
    frame.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox("all"))



# Create Label
label1 = Label( root , text = "Disease Prediction for Breast Cancer Data Set " )
label1.pack()

# Dropdown menu options
options = [
	"Random Forest",
	"Neural Network"
]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set( "Select a ML model" )

# Create Dropdown menu
drop = OptionMenu( root , clicked , *options )
drop.pack()

# Create button, it will change label text
button = Button( root , text = "Train" , command = show ).pack()

# Create Label
label = Label( root , text = " " )
label.pack()


# Create a button with the text "Click me"
# and specify the function to be called when the button is clicked
button1 = Button(root, text="Input parameters", command= on_click ).pack()

# Execute tkinter
root.mainloop()
