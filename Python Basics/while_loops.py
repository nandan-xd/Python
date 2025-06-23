i = 0
while(i<=3):
    print(i)
    i = i + 1
print("Done with the loop.")

x = int(input("Enter initial value of x : "))
while(x<=50):
    x  = int(input("Enter the number : "))
    print(x)

    if x<=50:
        print(x, "<= 50")
    else:
        print(x, "> 50")


# Decrementing while loop 
count = 5
while (count > 0):
    print(count)
    count = count - 1
else:                                 #We can also use else with while, when while loop will break/ gives false value else will run
    print("Loop ended at 1")

