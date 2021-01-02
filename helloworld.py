# def plus(*args):
#     result = 0
#     for number in args:
#         result += number
#     print(result)


# plus(1, 2, 1, 1,1,1,2,3,1,2, 6, 7, 8, 5, 4, 3, 3, 2, 1, 1)

#Object Oriented Programming
class Car():   #blueprint


    def __init__(self, **kwargs):
        print(kwargs.get)
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4 
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"



class Convertible(Car):   #blueprint

    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "taking off"

    def __str__(self):
        return f"Car with no roof"


porsche = Convertible(color = "green", price = "$40")
print(porsche.color)


# Porsche = Car()   #instance
# Porsche.color = "Red"

# ferrari = Car()    #instance
# ferrari.color = "Yellow"

# mini = Car()
# mini.color = "White"

# print(Porsche.color)