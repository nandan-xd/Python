x = 4
y = 'Hello World'

def Hello() :
    x = 5
    print(f'This is local variable {x}') 
    print(y)

Hello()
print(f'This is global variable {x}')

def Hello2() :
    global x
    x = 6
    print(f'This is new global variable {x}')

Hello2()
    