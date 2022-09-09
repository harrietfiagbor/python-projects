from tkinter import *

window = Tk()
window.title("Miles to Kilometre converter")
window.minsize(width=300, height=150)
window.config(padx=50, pady=50)


def calculate_miles_to_km():
    miles = int(entry.get())
    km = miles * 1.609
    label_4.config(text=km)


label_1 = Label(text="is equal to")
label_1.grid(row=1, column=0)
label_1.config(padx=10, pady=10)

label_2 = Label(text="Miles")
label_2.grid(row=0, column=2)
label_2.config(padx=10, pady=10)

label_3 = Label(text="Km")
label_3.grid(row=1, column=2)
label_3.config(padx=10, pady=10)

label_4 = Label(text="0")
label_4.grid(row=1, column=1)
label_4.config(padx=10, pady=10)

button = Button(text="Calculate", command=calculate_miles_to_km)
button.grid(row=2, column=1)

entry = Entry(width=10)
entry.grid(row=0, column=1)

window.mainloop()
