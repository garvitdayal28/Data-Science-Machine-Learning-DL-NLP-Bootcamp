def square(n):
    for i in range(n):
      yield i**2

print(square(2))

#one way to iterate through yield

for i in square(4):
    print(i)

print("\n------------------------------\n")


# or use next function
a = square(4)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
    
def my_generator():
    yield 1
    yield 2
    yield 3
    
print("\n**************************\n")
gen = my_generator()
print(gen)

for val in gen:
    print(val)

print("\n------------------------------\n")

gen = my_generator() # --> this is a way to reset the iteration but it reality it just starts a new interation

print(next(gen))
print(next(gen))
print(next(gen))



##  Practical : Reading Large Files

def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
            
for line in read_large_file("verylargefile.txt"):
    print(line.strip())