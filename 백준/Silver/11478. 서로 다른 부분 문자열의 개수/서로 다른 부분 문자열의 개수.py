import sys

char = sys.stdin.readline().strip()

set_char = set()
for i in range(0, len(char)):
    for j in range(i + 1, len(char) + 1):
        target = char[i:j]
        set_char.add(target)

print(len(set_char))