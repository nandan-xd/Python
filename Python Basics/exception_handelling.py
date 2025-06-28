a = input('Enter a number : ')
print(f'Multiplication table of {a} is ')
try :                                            #try….. except blocks are used in python
    for i in range(1, 11):                       # to handle errors and exceptions.
        print(f'{int(a)}X{i} = {int(a)*i}')      # The code in try block runs when there is no error.
except :                                         # If the try block catches the error, then the except block is executed.
    print('Invalid input')

print('Another lines of code')