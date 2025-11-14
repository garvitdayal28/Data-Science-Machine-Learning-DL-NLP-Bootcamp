

class Car():
    def __init__(self, windows, doors, enginetype):
        self.windows=windows
        self.doors=doors
        self.enginetype=enginetype
        
    def drive(self):
        print(f"The person will drive the {self.enginetype} car")
        
car1=Car(4,5,"petrol")
car1.drive()

class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors, enginetype) #super is used to inherit property of parent class
        self.is_selfdriving=is_selfdriving
        
    def selfdriving(self):
        print(f"Tesla supports self driving : {self.is_selfdriving}")
        
tesla1=Tesla(4,4,"electric",True)
tesla1.selfdriving()
tesla1.drive()

#mutliple inheritance ----> inherits from more than one class

#Base class 1
class Animal():
    def __init__(self, name):
        self.name = name
        print(f"Name of the animal is {self.name}")
        
    def speak(self):
        print("Subclass must implement this method")
        
        
#Base class 2
class Pet():
    def __init__(self, owner):
        self.owner = owner
        
#Derived class    
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)
        Pet.__init__(self, owner)
        
    def speak(self):
        return f"{self.name} says woof"
    
dog=Dog("rocket", "alex")
print(dog.speak())