# Exercise 2 - Good Morning Sir!

import time
time = time.strftime('%H:%M:%S')
print(time)

if ("00.00.00" <= time < "12.00.00") :
    print("Good Morning Sir!")
elif ("12.00.00" <= time < "17.00.00") :
    print("Good Afternoon Sir!")
elif ("17.00.00" <= time < "20.00.00") :
    print("Good Evening Sir!")
else :
    print("Good Night Sir!")