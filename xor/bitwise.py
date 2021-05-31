data = 'label'
a = ''
for i in data:
    a += chr(ord(i) ^ 13)
print(a)
