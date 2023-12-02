import sys

stack = []
answer = []
cnt = 1
check = True

n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())

    while cnt <= num:
        stack.append(cnt)
        answer.append("+")
        cnt += 1
        
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        check = False
        break

if check == True:
    print("\n".join(answer))