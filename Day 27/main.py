from tkinter import *

# Create a window
window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label Component
my_label = Label(text="I am a Label", font=("Times New Roman", 24, "bold"))

# Add the component to the screen
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")

def button_click():
    print("Clicked the button")
    my_label["text"] = input.get()

# Button Component
button = Button(text="Click Me", font=("Times New Roman", 12, "normal"), command=button_click)

# Add the button to the screen
button.pack()

# Entry Component
input = Entry(width=10)
input.pack()

# Makes the window show till you exit
window.mainloop()

