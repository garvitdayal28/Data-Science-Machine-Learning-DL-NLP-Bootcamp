class Error(Exception):
    pass

class dobException(Error):
    pass

year = int(input("Enter your birth year: "))
age = 2025 - year

try:
    if age<=30 and age>=20:
     print("The age is valid and so you can apply for exam")
    
    else:
     raise dobException

except:
    print("Sorry, Your age should be between 20-30")