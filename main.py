from tkinter import *


def converter():
    miles = float(miles_input.get())
    km = miles * 1.609
    result.config(text=f"{km}")


window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)


label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

label_km = Label(text="Km")
label_km.grid(column=2, row=1)

button = Button(text="Calculate", command=converter)
button.grid(column=1, row=2)

miles_input = Entry(width=8)
miles_input.grid(column=1, row=0)

result = Label(text="0")
result.grid(column=1, row=1)


window.mainloop()
