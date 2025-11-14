
#Sub topic ---->Method overriding

#Base class
class Animal:
    def speak(self):
        return "Sound of the animal"
    
#Derived class 1
class Dog(Animal):
    def speak(self): #-----> this is callde a method
        return "Woof!!!"
    
#Derived class 2
class Cat(Animal):
    def speak(self):
        return "Meow!!!"
    
#Function that demonstrates polymorphism
def animal_speak(animal):
    print(animal.speak())
    
dog=Dog()
cat=Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)

#Polymorphism with functions and methods

#Parent class
class Shape:
    def area(self):
        return "The area of the figure"
  
#Derived class 1  
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    
    #when is {shape} is called it will return string instead of memory address because of this method
    def __str__(self):
        return "rectangle"
    
#Derived class 2
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * 3.14
    
    def __str__(self):
        return "circle"
    
#Function that demonstrates polymorphism

def display_area(shape):
    print(f"The area of {shape} is {shape.area()}")
    
rectange = Rectangle(30,20)
circle = Circle(3)

print(rectange.area())
print(circle.area())

display_area(rectange)
display_area(circle)


#Polymorphism with abstract base class

from abc import ABC, abstractmethod

#Define an abstract class
class Vehical(ABC):
    @abstractmethod
    def start_engine(self):
        pass
 
#Derived class 1   
class Car(Vehical):
    def start_engine(self):
        return "Car engine started"
    
#Derived class 2    
class Motorcycle(Vehical):
    def start_engine(self):
        return "Motorcycle engine started"
 
#Function to demonstrate polymoephism
def start_vehical(vehical):
    print(vehical.start_engine()) 
    
    
#create objedts of car and motorcycle
car = Car()
motorcylce = Motorcycle()

start_vehical(car)
start_vehical(motorcylce)