# def double(x) :    # this is a function
#     return(x*2)

double = lambda x : x*2  # this is lambda function

print(double(5))

avg = lambda x, y : (x+y)/2
print(avg(2, 5))

def appl(fx, value) :
    return fx(value)

print(appl(lambda x : x*x*x, 2))

# Lambda function to calculate the product of two numbers,
# with additional print statement
product = lambda x, y: print(f'{x} * {y} = {x * y}')
print(product(4, 5))
x = int(input('Enter x : '))
y = int(input('Enter y : '))
product(x, y)
