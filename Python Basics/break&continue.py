# break
for i in range(15):
   if (i == 11) :
    break                       #This will break the loop at 10.
   print("5 x", i, "=", 5*i)   
i = i + 1

# continue
for i in range(15):
   if (i == 11) :
    print("Skipped")
    continue                       #This will skip the iteration and and will continue
   print("5 x", i, "=", 5*i)   
i = i + 1
