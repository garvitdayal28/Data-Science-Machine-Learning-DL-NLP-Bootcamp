class Car:
    def __init__(self,name,window,speed):
        self.name=name
        self.window=window
        self.speed=speed
        
    def display_speed(self):
        print(f"The speed of {self.name} is {self.speed} km/h")

car1=Car("Audi",4,140)

print(car1)
print(car1.name)
print(car1.window)
print(car1.speed)

car1.display_speed()