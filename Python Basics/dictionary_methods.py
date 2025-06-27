info = {'name':'Karan', 'age':19, 'eligible':True}   #update()
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}  #clear()
info.clear()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True}  #pop()
info.pop('eligible')
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003} #popitem()
info.popitem()
print(info)

info = {'name':'Karan', 'age':19, 'eligible':True, 'DOB':2003} #del dict()
del info
print(info)