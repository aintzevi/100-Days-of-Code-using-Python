# These are UNLIMITED POSITIONAL ARGUMENTS (works by position, think C) : *args

def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(1, 7))

# These are UNLIMITED KEYWORDED ARGUMENTS : **kwargs

# kwargs is a dictionary
def print_kwargs(**kwargs):
    # I can iterate as usually, or by name
    for key, value in kwargs.items():
        print(key)
        print(value)

    # or
    print(kwargs['add']) # will print the value of named argument "add" if it exists - else ERROR THROW


def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mul"]
    print(n)


calculate(2, add=3, mul=5)


class Car:
    def __init__(self, **kw):
        # if me self.make = kw["make"] and make is not specified, the call would crash. Instead we use .get
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
