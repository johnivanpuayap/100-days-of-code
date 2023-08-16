# Create the logging_decorator() function 👇
def logging_decorator(function):
    def wrapper(*args):
        print(function.__name__)
        return function(*args)
    return wrapper


# Use the decorator 👇
@logging_decorator
def multiply(*args):
    product = 1
    for arg in args:
        product *= arg

    return product


print(multiply(4, 5, 6))
