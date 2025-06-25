# Manipulating Tuples

countries = ("Spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")       #add item 
temp.pop(3)                 #remove item
temp[2] = "Finland"         #change item
countries = tuple(temp)
print(countries)

countries = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries + countries2
print(southEastAsia)

#tuple.count()
num = (2, 4, 3, 3, 4, 5, 1, 2, 4)
res = num.count(3)
print(res)

#tuple.index()
res1 = num.index(3, 1, 6)  
print(res1)

