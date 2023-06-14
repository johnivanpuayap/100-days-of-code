# Simple Function
def greet():
    print("Hello World!")
    print("How do you do user?")
    print("Isn't the weather nice today?")
greet()

# Function that allow for input

def greet_with_input(name):
    print(f"Hello {name}!")
    print(f"How do you do {name}?")
greet_with_input("Ivan")

# Function with more than one input

def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"What is it like in {location}?")

greet_with("Ivan", "Cebu")

# Function with keyword arguments
greet_with(location="Cebu", name="Ivan")