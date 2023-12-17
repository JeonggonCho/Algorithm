import sys

s = sys.stdin.readline().strip()

li = []
for i in range(len(s)):
    char = s[i::]
    li.append(char)

li.sort()

print('\n'.join(li))