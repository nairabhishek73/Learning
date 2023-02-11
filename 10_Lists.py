names = ["ab","bc","cd","de","fg"]
print(names)
print(names[0]) #0 is the first name of the list
print(names[-1]) # is the last name of the list, bit odd
names[0]= "az" #calls the first variable and allows you to alter it
print(names)
print(names[0:3]) #will print the first 3 names, not 4. Always have to do +1\
print(names)
#notice that here the list retains its original length, but the altered ab to az remains altered
#??When i removed the square brackets everywhere, everything worked except for the replacement. (lines 5 and 6)


