def calc1(matrix, numbers):
    return matrix[numbers[0] - 1][numbers[1] - 1]


def calc2(matrix, num):
    for l in range(len(matrix)):
        for m in range(len(matrix[l])):
            if matrix[l][m] == num:
                numbers = [l + 1, m + 1]
                return numbers


def calc3(matrix, num1, num2):
    numbers1 = calc2(matrix, num1)
    numbers2 = calc2(matrix, num2)
    numbers3 = (numbers1[0] + numbers2[0], numbers1[1] + numbers2[1])
    result = calc1(matrix, numbers3)
    return result


matrix = []
for _ in range(300):
    matrix.append([0 for j in range(300)])

number = 1
for k in range(300):
    position = [0, k]
    while 0 <= position[0] < 300 and 0 <= position[1] < 300:
        matrix[position[0]][position[1]] = number
        position[0] += 1
        position[1] -= 1
        number += 1

T = int(input())

for i in range(1, T+1):
    p, q = map(int, input().split())
    answer = calc3(matrix, p, q)
    print(f'#{i} {answer}')