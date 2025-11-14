from abc import ABC, abstractmethod
 
#Abstract base class
class Vehical(ABC):
    def drive(self):
         print("The vehical is used for driving")
         
    @abstractmethod
    def start_engine(self):
        pass
    
#child class     
class Car(Vehical):
    def start_engine(self):
        print("Car engine started")
        
def operate_vehical(vehical):
         vehical.start_engine()
         vehical.drive()
         
car=Car()
operate_vehical(car)