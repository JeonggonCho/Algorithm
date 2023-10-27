results = []

T = int(input())

for i in range(1, T+1):
    seq = [1, 1, 1, 2, 2]
    N = int(input())
    if len(seq) >= N:
        result = seq[N-1]
        results.append(f'#{i} {result}')
    else:
        while len(seq) != N:
            result = seq[-1] + seq[-5]
            seq.append(result)
        results.append(f'#{i} {result}')

for j in results:
    print(j)