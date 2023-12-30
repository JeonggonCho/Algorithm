import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

check = False
while len(S) != len(T):
    if T[-1] == "A":
        T = T[0:len(T) - 1]
        if T == S:
            check = True
            result = 1
            break
    elif T[-1] == "B":
        T = T[0:len(T) - 1]
        T = T[::-1]
        if T == S:
            check = True
            result = 1
            break
    if check == True:
        break
else:
    result = 0

print(result)