f = open('myfile.txt', 'r')   #redlines()
while True:
    line = f.readline()
    if not line:
        break
    print(line)

f = open('myfile.txt', 'w')                   #writelines()
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

f = open('myfile.txt', 'w')             #write()
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()