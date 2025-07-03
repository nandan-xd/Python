from functools import reduce

def sum(x, y) :
   return x+y 
l = [1, 2, 3, 4, 5]
suml = reduce(sum, l)
print(suml)
