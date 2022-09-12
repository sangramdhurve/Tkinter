from tkinter import *

window = Tk()
window.title("my first program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="Button get's clicked", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=0)

my_label["text"] = "new text"
my_label.config(text="New Text")  # there are two methods are there for changing arg.


# Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me dude", command=button_clicked)
button.grid(column=2, row=0)

# Entry
input = Entry(width=10)
input.grid(column=3, row=2)
print(input.get())

window.mainloop()
