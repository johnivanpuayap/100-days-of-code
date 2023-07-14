import tkinter

# Create a window
window = tkinter.Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label Component
my_label = tkinter.Label(text="I am a Label", font=("Times New Roman", 24, "bold"))

# Add the component to the screen
my_label.pack(expand=True)

# Makes the window show till you exit iy
window.mainloop()

