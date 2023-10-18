def check_palindrome1(N, matrix):
    cnt = 0
    for k in matrix:
        for l in range(9-N):
            char = ''.join(k[l:l+N])
            if char == char[::-1]:
                cnt += 1
    return cnt


def check_palindrome2(N, matrix):
    cnt = 0
    for m in range(8):
        li = []
        for n in matrix:
            li.append(n[m])
        for o in range(9-N):
            char = ''.join(li[o:o+N])
            if char == char[::-1]:
                cnt += 1
    return cnt


results = []

for i in range(1, 11):
    cnt = 0
    N = int(input())
    matrix = []
    for j in range(8):
        li = list(input())
        matrix.append(li)

    cnt += check_palindrome1(N, matrix)
    cnt += check_palindrome2(N, matrix)

    results.append(f'#{i} {cnt}')

for p in results:
    print(p)