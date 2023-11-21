results = []

for i in range(1, 11):
    matrix = []
    result = 0
    n = int(input())

    for j in range(n):
        magnets = list(map(int, input().split()))
        matrix.append(magnets)

    for k in range(n):
        magnets_rows = []
        for l in matrix:
            if l[k] != 0:
                magnets_rows.append(l[k])
        seq = ''.join(map(str, magnets_rows))
        result += seq.count('12')

    results.append(f'#{i} {result}')

for m in results:
    print(m)