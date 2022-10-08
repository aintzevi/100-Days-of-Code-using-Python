import tkinter

# creates the window, but since nothing else happens, it terminates
window = tkinter.Tk()

window.title("My first Tkinter Program")
window.minsize(width=500, height=300)

# Label

# Creates the label, but still not displayed
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24))
# To display the label we need to say how to display it on the screen
# my_label.pack(side="left")

# By removing the side argument, the window will simply display the items one after the other as they are being added
my_label.pack()

# puts the label in the center of the window

# We can also change the properties of an item dictionary style or using the config function with keyworded args
my_label["text"] = "New text"
my_label.config(text="New new text")


# ADVANCED PYTHON ARGUMENTS
# We can add default values to the function, and if need be use a different arg value when calling the function.
# Optional arguments are ones that already have a default value

# FOR MANY POSITIONAL ARGUMENTS: *args
# The asterisk means you can add any number of arguments

def button_clicked():
    print("I got clicked!")
    new_text = input.get()
    my_label.config(text=new_text)


# The command arg is the listener for the button. Again here we are using the function name, so no parenthesis needed
button = tkinter.Button(text="Click me", command=button_clicked)
button.pack()

# Entry component, where the user can give input using our GUI
input = tkinter.Entry(width=20)
input.pack()

multi_line_input = tkinter.Entry()


# To keep the window open, we need the
window.mainloop()
# function. This must be the last thing to run!
