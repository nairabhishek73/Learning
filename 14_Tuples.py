#Immutable lists=tupples
numbers= (1,2,3,3)
print(numbers)

print(numbers.count(3))
print(numbers.index(3))

#numbers. any of the underscored fields are advanced, learn later

numbers[0]= 10 #will throw error since you cant change a tuple
#"numbers." will now not show you append and insert- because its a tuple and you cant change it.
# had checked this earlier in lists, now understanding why that happened

#tuples are rarely used, only if you want a list to stay static, mostly we'll use lists only