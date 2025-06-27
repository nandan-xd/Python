dict = {
    'name':'Nandan',
    'age': 17,
    'Country':'India',
}
print(dict)
print(dict['age'])
print(dict.get('city'))
print(dict.keys())
print(dict.values())
for key in dict.keys() :
    print(f'The value corresponding to the {key} is {dict[key]}')
print(dict.items())