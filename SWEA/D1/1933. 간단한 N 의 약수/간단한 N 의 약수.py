N = int(input())
list1 = []

for i in range(1, N+1):
    if N % i == 0:
        list1.append(i)
print(*sorted(list1))