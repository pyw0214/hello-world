# def plus(*args):
#     result = 0
#     for number in args:
#         result += number
#     print(result)


# plus(1, 2, 1, 1,1,1,2,3,1,2, 6, 7, 8, 5, 4, 3, 3, 2, 1, 1)

#Object Oriented Programming
class Car():   #blueprint
    wheels = 4
    doors = 4
    windows = 4
    seats = 4

    def start(self):   #method  = a function in class
        print(self.color)
        print("I started")

porsche = Car()
porsche.color = "Red Sexy Red"
porsche.start()


# Porsche = Car()   #instance
# Porsche.color = "Red"

# ferrari = Car()    #instance
# ferrari.color = "Yellow"

# mini = Car()
# mini.color = "White"

# print(Porsche.color)