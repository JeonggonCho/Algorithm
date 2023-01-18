T = int(input())

for i in range(T):
    R, S = input().split()
    char = ''
    for j in S:
        char += (j * int(R))
    print(char)