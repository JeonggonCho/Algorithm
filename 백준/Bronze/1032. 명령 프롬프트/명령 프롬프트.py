import sys

N = int(sys.stdin.readline())

result = ''

for i in range(N):
    char = sys.stdin.readline().strip()
    compare = ''

    if not result:
        result = char

    else:
        for i in range(len(char)):
            if char[i] == result[i] and result[i] != '?':
                compare += char[i]
            else:
                compare += '?'
        result = compare

print(result)