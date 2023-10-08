def digital_root(num):
    if num == 0:
        return 0
    else:
        return 1 + (num - 1) % 9

T = int(input())

results = []
for _ in range(T):
    n = int(input())
    results.append(digital_root(n))

for i in range(1, T+1):
    print(f'#{i} {results[i-1]}')