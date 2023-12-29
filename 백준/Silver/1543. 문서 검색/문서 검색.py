import sys

char1 = sys.stdin.readline().strip()
char2 = sys.stdin.readline().strip()

answer = 0
while char1:
    if char1[0:len(char2)] != char2:
        char1 = char1[1::]
    else:
        answer += 1
        char1 = char1[len(char2)::]
    if len(char1) < len(char2):
        break
print(answer)