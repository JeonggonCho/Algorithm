T = int(input())

for i in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    print(sum(numbers))