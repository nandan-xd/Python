l = [1, 2, 3, 4, 5, 6]

even = lambda x: x%2==0

newl = list(filter(even, l))
print(newl)