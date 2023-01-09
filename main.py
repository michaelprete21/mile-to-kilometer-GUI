from tkinter import *

def calculate_KM():
    text_miles = f_input.get()
    miles_km = int(text_miles) * 1.60934
    km_equals["text"] = (f"{miles_km}")


window = Tk()
window.title("Mile to KM Converter")
window.config(padx=20, pady=20)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

f_input = Entry(width=30)
f_input.grid(column=1, row=0)

equal = Label(text="Is Equal To")
equal.grid(column=0, row=1)

km_equals = Label(text=f"Output")
km_equals.grid(column=1, row=1)

km = Label(text="KM")
km.grid(column=2, row=1)

button_calculate = Button(text="Calculate", command=calculate_KM)
button_calculate.grid(column=1, row=2)















window.mainloop()
