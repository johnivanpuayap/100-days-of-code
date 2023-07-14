# args
# you can change the 'args' word to anything that you want but the asterisk(*) should always be there
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1, 2, 3, 4, 5))