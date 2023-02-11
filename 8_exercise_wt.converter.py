#attempt
wt=float(input("Weight:"))
metric=input("(K)g or (L)bs:")
if metric=="l" or metric=="L":
    print(round(wt * 0.453592, 2))
elif metric=="K" or metric=="k":
    print(round(wt*2.20462,2))
else:
    print("Please type 'k' or 'K' for Kg and 'l' or 'L' for Lbs")
#suggested
wt=float(input("Weight:"))
metric=input("(K)g or (L)bs:")
if metric.upper()=="K":
    converted= round(wt/0.45, 2)
    print("Weight in Lbs:" + str(converted))
else:
    converted = round(wt * 0.45, 2)
    print("Weight in Kgs:" + str(converted))

