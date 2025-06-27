# Quick Quiz: Write a program to print the Fibonacci sequence
#f(0) = 0
#f(1) = 1
#f(n) = f(n-1) + f(n-2)

def fibonacci(n) :
    if n==0 :
        return 0
    elif n==1 :
        return 1
    else :
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(3))
print(fibonacci(4))
print(fibonacci(5))