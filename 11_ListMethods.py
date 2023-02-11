#objects and methods, "a" is an object and "a." shows all the methods
#similarly lists are objects on which you can run methods
numbers= [1,2,3,4,5]
numbers.append(6) #add 6 at the end
print(numbers)
numbers.insert(0,-1)
#if the pop up doesn't show you parameters(instructions) then hit cmd+p to see
#for intert, "object:_T" indicates that the object can be of any type; string,boolean,integer
print(numbers)
#notice here that the list is permanently alters, 2 new values have been added permanently
numbers.remove(3)
print(numbers)
print(1 in numbers) #generates boolean T/F
print(len(numbers)) #returns the number of elements in a list
numbers.clear()
print(numbers)

