from tkinter import *

CONSTANT = 1.609344

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entries
input = Entry(width=5)
input.grid(column=1, row=0)

# Labels
miles_label = Label(text="miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

result_label = Label(text="0")
result_label.grid(column=1, row=1)

label = Label(text="is equal to")
label.grid(column=0, row=1)


# Calculation function
def miles_to_km():
    miles = float(input.get())
    km = miles * CONSTANT
    result_label.config(text=f"{km}")


calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
