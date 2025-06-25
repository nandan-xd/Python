list = [4, 5, 8, "Nandan", True]
print(type(list))
print(list)

#Check whether an item is present in list

if 7 in list:
    print("Yes")         #this is done using 'in' keyword
else:
    print("No")


# Range of Index

animals = ['dog', 'cat', 'horse', 'lion', 'tiger', 'jaguar']
print(animals[0:5:2])         #listName[start : end : jumpIndex]
print(animals[::2])         
print(animals[:-1:2])      


# List Comprehension
lst = ['Steve', 'Tony', 'Bruce', 'Thor', 'Clint', 'Natasha']
lst2 = [item for item in lst if "t" in item ]
print(lst2)
lst3 = [item for item in lst if (len(item) > 4)]
print(lst3)
lst4 = [i for i in range(10) if i%2==0]
print(lst4)