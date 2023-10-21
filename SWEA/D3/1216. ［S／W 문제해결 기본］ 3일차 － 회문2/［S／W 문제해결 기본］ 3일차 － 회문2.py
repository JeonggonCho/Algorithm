def horizontal_pelindrome_max_length(matrix, length):
    for m in matrix:
        for n in range(0, 100 - length + 1):
            char = ''.join(m[n:n + length])
            if char == char[::-1]:
                return True
    return False

def vetical_pelindrome_max_length(matrix, length):
    for o in range(0, 100):
        li = []
        for p in matrix:
            li.append(p[o])
        for q in range(0, 100 - length + 1):
            char = ''.join(li[q:q + length])
            if char == char[::-1]:
                return True
    return False

results = []

for i in range(1, 11):
    N = int(input())
    matrix = []

    for j in range(100):
        char = list(input())
        matrix.append(char)

    for k in range(100, 0, -1):
        check_1 = horizontal_pelindrome_max_length(matrix, k)
        check_2 = vetical_pelindrome_max_length(matrix, k)

        if check_1 or check_2:
            results.append(f'#{i} {k}')
            break

for l in results:
    print(l)