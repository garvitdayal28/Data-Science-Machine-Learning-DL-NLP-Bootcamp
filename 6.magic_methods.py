class Person:
    pass

person = Person()
dir(person)


#Basic Magic Methods
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} year old"
        
    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"
person = Person("Garvit",18)
print(person)
print(repr(person))