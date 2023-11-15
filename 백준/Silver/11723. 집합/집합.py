import sys

M = int(sys.stdin.readline())
S = set()

for i in range(M):
    prompt = sys.stdin.readline().split()

    if len(prompt) == 1:
        order = prompt[0]
        if order == "all":
            S = set([j for j in range(1, 21)])
            
        elif order == "empty":
            S = set()
            
    else:
        order, num = prompt[0], int(prompt[1])
        if order == "add":
            S.add(num)

        elif order == "remove":
            if num in S:
                S.discard(num)

        elif order == "check":
            print(1 if num in S else 0)

        elif order == "toggle":
            if num in S:
                S.discard(num)
            else:
                S.add(num)