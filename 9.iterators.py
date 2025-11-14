list = [1,2,3,4,5,6,7]

for i in list:
    print(i)
    
#creating a iterator

iterator = iter(list)
print(type(iterator))

#iterate through all the 
try:
    
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    print(next(iterator))
    
except StopIteration:
    print("StopIteration Error")
    print("There are no elements in the iterator")