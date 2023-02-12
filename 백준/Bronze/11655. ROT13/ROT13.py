import sys

result = ''

s = sys.stdin.readline()

for i in s:
    if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
        if 90 < ord(i) + 13 <= 103 or 122 <ord(i) + 13 <= 135:
            result += chr(ord(i) + 13 - 26)
        else:
            result += chr(ord(i) + 13)
    else:
        result += i
print(result)