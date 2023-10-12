def getNumList(maxNum):
    num = 1
    for i in range(50):
        print(f"{num}.png", end=' ')
        if(num * 10 <= maxNum):
            num *= 10
        elif(num + 1 <= maxNum):
            if num % 10 == 9:
                num //= 10
                if(num == 0):
                    break
            num += 1
        else:
            num //= 10
            if(num == 0):
                break
            num += 1
            
T = int(input())

for t in range(1, T + 1):
    N = int(input())
    print(f"#{t}", end=' ')
    getNumList(N)
    print()