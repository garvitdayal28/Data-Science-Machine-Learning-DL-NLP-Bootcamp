## Function copy
print("------Function Copy-------\n")
def welcome():
    return "welcome to advance python course"

wel = welcome # this creates a copy of the original function
print(wel)
print(wel())


del welcome # deleting the function

print(wel) # copy still exists after deleting the original function
print(wel())

print("\n**********************************\n")

## Closures

    #function inside a function / method within a method
print("\n--------Closures-------\n")

def main_welcome(msg):
    #msg = "Welcome User"
    def sub_welcome_method():
        print("Welcome to the advance python course")
        print(msg)
        print("Please learn these concepts properly")
        
    return sub_welcome_method()

main_welcome("Welcome everyone")

print("\n**********************************\n")

def main_welcome_v2(func):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func("Welcome everyone to this tutorial")
        print("Please learn these concepts properly")
        
    return sub_welcome_method()

main_welcome_v2(print)


print("\n**********************************\n")

def main_welcome_v3(func, lst):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        print(func(lst))
        print("Please learn these concepts properly")
        
    return sub_welcome_method()

main_welcome_v3(len, [3,5,9,61,2,16,6])


## Decorator

print("\n**********************************\n")

def main_welcome_v4(func):
    def sub_welcome_method():
        print("Welcome to the advance python course")
        func()
        print("Please learn these concepts properly")
        
    return sub_welcome_method()

def course_introduction():
    print("This is a advacne python course")
    
main_welcome_v4(course_introduction)

# now we'll do the exact thing we did above using decorators
print("\n-----Decorators------\n")


@main_welcome_v4
def course_introduction():  #this will go inside main_welcome_v4 as a parameter
    print("This is a advacne python course")
    
    
# another example

print("\n**********************************\n")

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called")
        func()
        print("Something is happening after the function is called")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!!!")
    
say_hello()

# Decorators with arguments


print("\n**********************************\n")

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs): #positional and keyword arguments 
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hello():
    print("hello!!")
    
say_hello()