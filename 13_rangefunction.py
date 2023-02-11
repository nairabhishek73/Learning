numbers= range(5)
print(numbers) #gives us "range(0,5)"- representation of values from 0 to 4

numbers= range(5)
for number in numbers:
    print(number)
#understanding now that 'number' is like a new varibale that we are creating and then using for..
#the first time in the for loop

numbers= range(5,10) #10 becomes the last value so will give 5 to 9
for number in numbers:
    print(number)

numbers= range(5,10,2) #2 becomes the step value so will give 5 7 9
for number in numbers:
    print(number)

numbers= range(5)
for number in range(5): #can also directly put range here,dont' need to create numbers variable
    print(number)

print(number) #so now this gave me the last value stored in number, which was 4.


