# Import modules
from tkinter import *
from PIL import Image, ImageTk

# Create object
root = Tk()

root.title('SC Final Project')

frame = Frame(root, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("image.jpeg"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()


scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )

scrollbar.config()



# Set the background color to blue
root.configure(bg="Blue")

# Adjust size
root.geometry("1000x1000")

# Create Label
label1 = Label(root, text="Disease Prediction for Breast Cancer Data Set ", font=("Arial", 23, "bold"), fg="red", bg="yellow")

# Add the label to the root window
label1.pack(padx=50)

# Functions :
# -----------

# Change the label text
def show():
    label.config(text=clicked.get())

# function that reads the output form_data.txt file and saves it as an output
def readform():
    try:
        # Read the input from the file and store it in variables
        with open('form_data.txt', 'r') as f:
            input1 = f.readline().strip()
            input2 = f.readline().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "form_data.txt file not found")
    else:
        # You can now use the input1 and input2 variables in your code
        print(input1)
        print(input2)

#Create function here for loading the dataset
def load_data():
    try:
        # Read the input from the file and store it in variables
        with open('form_data.txt', 'r') as f:
            input1 = f.readline().strip()
            input2 = f.readline().strip()
    except FileNotFoundError:
        messagebox.showerror("Error", "form_data.txt file not found")
    else:
        # You can now use the input1 and input2 variables in your code
        print(input1)
        print(input2)

    return None 

# Rewrite this function name as create_nn
def create_nn(nn_params):

    num_nodes = nn_params[0]
    num_layers = nn_params[1]
    activation = nn_params[2]
    optimizer = nn_params[3]
    loss = nn_params[4]
    test_size = nn_params[6]
    bacth_size = nn_params[7]
    epochs = nn_params[8]

    label1 = Label(root, text=epochs, font=("Arial", 23, "bold"), fg="red", bg="yellow")

    with open('form_data.txt', 'a') as text_file:
        text_file.write(input1 + '\n')
        text_file.write(input2 + '\n')

# model parameters function on click
def submit(options):

    if options == 'Random Forest':
        print('In Progress')
    else:
        input_label = Label(root, text="Neural Network")
        # Create the input fields
        # Txt entry that takes in dataset directory
        dataset_dir = Entry(root, text="Enter dataset directory (String) : ").pack()
        # lOAD the dataset
        dataset_load_button = Button(root, text='Load Dataset', command=load_data).pack()

        num_nodes_label = Label(root, text="Enter number of nodes (List) : ").pack()
        num_nodes = Entry(root).pack()

        num_layers_label = Label(root, text="Enter number of layers (List) : ").pack()
        num_layers = Entry(root).pack()
        
        activation_label = Label(root, text="Enter activation function for each layer (List) : ").pack()
        activation = Entry(root).pack()
        
        optimizer_label = Label(root, text="Enter optimization algorithm (String) : ").pack()
        optimizer = Entry(root).pack()

        loss_label = Label(root, text="Enter type of optimizer (String) : ").pack()
        loss = Entry(root).pack()
        
        test_size_label = Label(root, text="Enter test size (Integer) : ").pack()
        test = Entry(root).pack()

        batch_size_label = Label(root, text="Enter batch size (Integer) : ").pack()
        batch_size = Entry(root).pack()

        epochs_label = Label(root, text="Enter number of epochs (Integer) : ").pack()
        epochs = Entry(root).pack()


        # Submit bitton to create the nerual network
        nn_params = {
            'num_nodes':num_nodes.get(),
            'num_layers':num_layers.get(),
            'activation':activation.get(),
            'optimizer':optimizer.get(),
            'loss':loss.get(),
            'test_size':test_size.get(),
            'batch_size':batch_size.get(),
            'epochs':epochs.get()
        }

        create_nn_button = Button(root, text='Create Neural Net', command=lambda: create_nn(nn_params)).pack()

# Create the Train button
#button3 = Button(root, text="Submit", font = ('Arial','14'), command=lambda: save_form(input1.get(), input2.get()))
#button3.pack()
    

# --------------

# Dropdown menu options
options = ["Random Forest","Neural Network"]

# datatype of menu text
clicked = StringVar()

# initial menu text
clicked.set("Select a Machine Learning model")

# Create Dropdown menu
drop = OptionMenu(root, clicked, *options, command=submit)
drop.pack()



# Create submit button, it will change label text
# button = Button( root , text = "Submit" , command = submit ).pack()

# Create Label for drop down after selection

# if clicked.get() == "Random Forest":
  #  label = Label(root, *options , text="Random Forest").pack()

    #label.pack()

# Create a button with the text "Input Parameters"
# and specify the function to be called when the button is clicked
# button1 = Button(root, text="Input parameters", command= on_click ).pack()

# Execute tkinter
root.mainloop()


