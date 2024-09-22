def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

# print(add(3, 5, 100))

def calculate(n, **kwargs):
    n += kwargs["add"]
    print(n)
    n*= kwargs["multiply"]
    print(n)
    
# calculate(2, add = 3, multiply=5)

class Car:
    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs["model"]

car1 = Car(make = "Nissan", model = "GT-R")
print(car1.model)


