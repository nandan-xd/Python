# READING A FILE

f = open('myfile.txt', 'r')
print(f)
text = f.read()
print(text)
f.close()

# WRITING A FILE

f = open('myfile.txt', 'w')
f.write('Hello, world!')
f.close()

with open('myfile.txt', 'w') as f:
  f.write("Hey I am inside with")