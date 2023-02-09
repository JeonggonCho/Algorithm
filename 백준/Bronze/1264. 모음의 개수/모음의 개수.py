import sys

vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

while True:
    char = sys.stdin.readline().strip()
    cnt = 0
    if char == '#':
        break
    for i in char:
        if i in vowel:
            cnt += 1
    print(cnt)