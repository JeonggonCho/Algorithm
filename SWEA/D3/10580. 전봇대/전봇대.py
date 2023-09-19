T = int(input())

for i in range(1, T+1):
    cnt = 0
    N = int(input())
    link = []
    for j in range(N):
        a, b = map(int, input().split())
        link.append([a, b])
    link.sort(key = lambda x : -x[0])
    length = len(link)
    for k in range(length):
        line = link.pop()
        for l in link:
            if l[1] < line[1]:
                cnt += 1
    print(f'#{i} {cnt}')