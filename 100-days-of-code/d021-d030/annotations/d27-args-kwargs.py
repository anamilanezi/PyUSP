# Positional arguments

def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5))

# Many keyword arguments

def using_kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)


using_kwargs(add=5, multiply=10)


def calculate(n, **kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n


# Using *args and **kwargs
def all_aboard(a, *args, **kw):
    print(a, args, kw)


all_aboard(4, 7, 3, 0, x=10, y=64)


# **kwargs on a class:

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model", "Not found")

my_car = Car(make="Nissan")
print(my_car.model)