char = input()
cnt = 0
list_char = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in list_char:
    char = char.replace(i, '_')
print(len(char))