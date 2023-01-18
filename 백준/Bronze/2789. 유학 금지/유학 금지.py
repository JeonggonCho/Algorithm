char = input()
char_re = ''
cam = 'CAMBRIDGE'

for i in char:
    if i not in cam:
        char_re += i
print(char_re)