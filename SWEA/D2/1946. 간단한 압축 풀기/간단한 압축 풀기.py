def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]

T = int(input())

for i in range(1, T+1):
    zip = []
    N = int(input())
    for j in range(N):
        alpha, num = input().split()
        for k in range(int(num)):
            zip.append(alpha)
    list_chunked = list_chunk(zip, 10)
    print(f'#{i}')
    for l in list_chunked:
        char = "".join(l)
        print(char)