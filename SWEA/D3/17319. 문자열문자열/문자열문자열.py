T = int(input())
results = []

for i in range(1, T+1):
    length = int(input())
    char = input()
    if length % 2 != 0:
        results.append(f'#{i} No')
    else:
        for j in range(length // 2):
            if char[j] != char[j + (length // 2)]:
                results.append(f'#{i} No')
                break
        else:
            results.append(f'#{i} Yes')

for k in results:
    print(k)