s1 = {1, 5, 7, 5}
s2 = {2, 4, 5, 6}
print(s1.union(s2))   #union
s1.update(s2)  #update
print(s1)

s3 = {1, 3, 5}
s4 = {1, 2, 4, 5}
print(s3.intersection(s4))      #intersection  
s3.intersection_update(s4)      #intersection_update 
print(s3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}             #symmetric_difference
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities.symmetric_difference(cities2)
print(cities3)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}         #symmetric_difference_update
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities.symmetric_difference_update(cities2)
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}     #difference
cities2 = {"Seoul", "Kabul", "Delhi"}
cities3 = cities.difference(cities2)
print(cities3)
 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}    #isdisjoint
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}    #The isdisjoint() method checks if items of 
print(cities.isdisjoint(cities2))                  #given set are present in another set.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi", "Seoul", "Kabul"}   #issuperset
cities2 = {"Seoul", "Kabul"}                                        #The issuperset() method checks 
print(cities.issuperset(cities2))                                   #if all the items of a particular 
cities3 = {"Seoul", "Madrid","Kabul"}                               #set are present in the original set.
print(cities.issuperset(cities3))

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}  #issubst
cities2 = {"Delhi", "Madrid"}                    #The issubset() method checks if all the items 
print(cities2.issubset(cities))                  #of the original set are present in the particular set.
 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"} #add()
cities.add("Helsinki")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"} #remove()/discard()
cities.remove("Tokyo")
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"} #pop()
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"} #clear - This method clears all items in the set and prints an empty set.
cities.clear()
print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"} #del
del cities
print(cities)