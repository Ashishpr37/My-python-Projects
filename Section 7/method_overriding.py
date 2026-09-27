'''
method overriding means that when there is a method of parent class which does some task and the child class of that parent class has the same method but it performs some other task for the object of the child class and not doing the parent class's method for the object of the child class. THis is method overriding
'''

'''
Create a parent class called Vehicle with a method:

start()

It should print:

Vehicle is starting

Then create a child class called Car that inherits from Vehicle.

The Car should override the start() method and print:

Car starts with a key

Finally:
    Create an object of Vehicle.
    Create an object of Car.
    Call start() on both objects.

Expected output-
    Vehicle is starting
    Car starts with a key
'''

class Vehicle: # parent class
    def __init__(self): # constructor
        pass

    def start(self): # Method of parent class
        print("Vehicle is starting")

# inheritance

class Car(Vehicle): # Child class
    def __init__(self): # constructor of child class
        super().__init__() # super method is calling the method of constructor of parent class
        pass

    def start(self): # Method of child class, We will do overriding of this method
        print("Car starts with a key")


vehicle1=Vehicle()
vehicle2=Car()

vehicle1.start()
vehicle2.start()