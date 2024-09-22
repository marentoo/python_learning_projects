from tkinter import *

window = Tk()

window.title("My first GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = Label(text = "I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0)


#Button
def button_clicked():
    print("I got clicked")
    text1 = "CLICKED"
    my_label.config(text=text1)

button = Button(text="Click Me", command=button_clicked)
button.grid(column=3, row=0)

#Second button
button2 = Button(text="something to do", command=button_clicked)
button2.grid(column=2, row=2)

#Entry
input_entry = Entry(width=10)
print(input_entry.get())
input_entry.grid(column=4, row=3)



window.mainloop()
