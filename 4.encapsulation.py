#Encapsulation with getter and setter method

#Public, protected and private variables

class Person:
    def __init__(self, name, age):
        self.name = name #---->public varialbe 
        self.age = age #---->public varialbe
        
person = Person("Garvit", 18)
print(person.name)
print(dir(person))

print("************************************")

class Human:
    def __init__(self, name, age, gender):
        self.__name = name #---->Private varialbe 
        self.__age = age #---->Private varialbe
        self.gender = gender #---->public varialbe
        
def get_name(human):
    return human._Human__name

human = Human("Garvit", 18, "Male")
print(dir(human))
print(human)
print(get_name(human))

print("************************************")

class Animal:
    def __init__(self, name, age):
        self._name = name #---->protected varialbe 
        self._age = age #---->protected varialbe
        
class Pet(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

pet = Pet('rocket', 34) 
print(pet._name)

print("************************************")

##Encapulation with getting and setter method

class Person:
    def __init__(self, name , age):
        self.__name=name #Private access modifier or variable
        self.__age=age #Private variable
     
     #getter method for name   
    def get_name(self):
        return self.__name
    
    #getter methods for age
    def get_age(self):
        return self.__age
    
    #setter methods for name
    def set_name(self, name):
        self.__name=name
    
    #setter method for age
    def set_age(self, age):
        if int(age>0):
            self.__age=age
        else:
            print("Age can't be negative.")
            
            
person= Person("Alex", 17)

#Access and modify private variables using getter and setter 

print(person.get_name())
print(person.get_age())

person.set_name("Gravvox")
print(person.get_name())

person.set_age(-18)
print(person.get_age())
