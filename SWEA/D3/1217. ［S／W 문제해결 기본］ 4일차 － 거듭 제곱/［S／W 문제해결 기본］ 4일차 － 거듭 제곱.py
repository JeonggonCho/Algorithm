def solution(a, b):
    return a ** b

for i in range(10):
    T = int(input())
    n, m = map(int, input().split())
    print(f'#{T} {solution(n, m)}')