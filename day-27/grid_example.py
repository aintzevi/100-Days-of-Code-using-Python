from tkinter import *

# Creating a new window and configurations
window = Tk()
window.title("Grid Example")
window.minsize(width=500, height=500)

# Labels
label = Label(text="This is some text")
label.config(text="This is new text")
label.grid(column=0, row=0)


# Buttons
def action():
    print("Do something")


# calls action() when pressed
button = Button(text="Button", command=action)
button.grid(column=1, row=1)

new_button = Button(text="New Button", command=action)
new_button.grid(column=2, row=0)

# Entries
input = Entry(width=10)
input.grid(column=3, row=2)

print(input.get())

window.mainloop()
