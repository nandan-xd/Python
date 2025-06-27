str = 'Hey my name is {0} and I am from {1}.'
country = 'India'
name = 'Nandan'
print(str.format(name, country))       #This is string formatting
print(f'Hey my name is {name} and I am from {country}.')   #This is f-string
print(f'Hey my name is {{name}} and I am from {{country}}.')   #adding double curly brackets will not print value of that var

print(f'{2 + 4}')