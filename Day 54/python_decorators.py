import time
# Python Decorator Function

def delay_decorator(function):

    def wrapper_function():
        time.sleep(2)
        function()
        function()
    return wrapper_function

@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

@delay_decorator
def say_greeting():
    print("How are you?")

say_greeting()

# Another way to use the decorator function if you don't want to use a syntactic sugar
decorated_function = delay_decorator(say_greeting)
decorated_function()