from tkinter import *

def button_click():
    print("Clicked the button")
    my_label["text"] = input.get()

# Create a window
window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label Component
my_label = Label(text="I am a Label", font=("Times New Roman", 24, "bold"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.config(padx=50, pady=50)

# Add the component to the screen
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)

# Button Component
button = Button(text="Click Me", font=("Times New Roman", 12, "normal"), command=button_click)
# button.pack()
button.grid(column=1, row=1)

# Entry Component
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

# Button Component
new_button = Button(text="New Button", font=("Times New Roman", 12, "normal"), command=button_click)
# button.pack()
new_button.grid(column=2, row=0)



# Layout Managers
# Pack will always start from the top and then pack every other widget just below the previous one.
# Place is all about precise positioning. You need to provide x-y values. (0,0) is at the top right corner.
# Grid, will divide your entire program into number of columns and rows equally. You need to provide a column and row values.
# You can't mix grid and pack

# Makes the window show till you exit
window.mainloop()

