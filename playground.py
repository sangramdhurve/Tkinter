def add(*anku):
    sun = 0
    for n in anku:
        sun += n
    return sun


# print(add(2, 4, 5, 6, 7, 5, 3 , 66, 3))


def calculate(n, **kwargs): # key word arguments
    # for (key, vlaue) in kwargs.items():
    #     print(key)
    #     print(vlaue)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(3, add=45, multiply=3)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") # get will help us from error
        self.model = kw.get("model")


my_car = Car(make="RObeto", model="first_copy")
print(my_car.make)
