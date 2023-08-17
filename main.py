from tkinter import *

window = Tk()
window.title('M to Km Converter')
window.config(padx=20, pady=20)
window.minsize(width=275, height=0)
window.eval('tk::PlaceWindow . Center')


# function to convert miles to km
def convert(miles):
    return miles * 1.60934


def calculate_button_click():
    if miles_input.get() == '':
        output_label['text'] = 'Error'
    else:
        output_label['text'] = convert(float(miles_input.get()))


font = ('Calibri', 12)

# Entry box
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text='Miles', font=font)
miles_label.grid(column=2, row=0)

equals_label = Label(text='is equal to ', font=font)
equals_label.grid(column=0, row=1)

output_label = Label(text=0, font=font)
output_label.grid(column=1, row=1)

km_label = Label(text='Km', font=font)
km_label.grid(column=2, row=1)

# Button
calculate_button = Button(text='Calculate', command=calculate_button_click)
calculate_button.grid(column=1, row=2)

window.mainloop()
