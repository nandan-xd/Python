# list.sort()
lst = [4, 534, 65, 3, 0, 21]
lst.sort()              
print(lst)
lst.sort(reverse=True)
print(lst)

# list.reverse()
lst1 = ['violate', 'green', 'blue', 'red']
lst1.reverse()
print(lst1)

# list.index() & list.count()
lst2 = ['Steve', 'Tony', 'Thor', 'Steve']
print(lst2.index('Tony'))
print(lst2.count('Steve'))

# list.copy()
lst3 = ['Steve', 'Tony', 'Thor', 'Steve']
lst3.copy()
print(lst3)

# list.append()
lst4 = [4, 6, 7, 8]
lst4.append(323)
print(lst4)

# list.insert()
lst5 = [1, 3, 4]
lst5.insert(1, 2)       #Now this will insert '2' at index 1.
print(lst5)

#list.extent(list2)
lst4.extend(lst5)   #lst5 will combine with lst4.
print(lst4)

# Concatenating two lists
lst6 = lst1 + lst2
print(lst6)