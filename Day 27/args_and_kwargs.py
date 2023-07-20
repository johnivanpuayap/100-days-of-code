# args
# you can change the 'args' word to anything that you want but the asterisk(*) should always be there
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(1, 2, 3, 4, 5))

# kwargs
# you can change the 'kwargs' word to anything that you want but the double asterisk(**) should always be there
def calculate(n, **kwargs):
    # print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    # print(n)

calculate(2, add=3, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

car = Car(make="Nissan", model="Skyline")
print(car.model)
print(car.make)