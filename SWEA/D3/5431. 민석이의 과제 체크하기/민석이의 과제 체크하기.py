T = int(input())

for i in range(1, T+1):
    n, k = map(int, input().split())
    students = set([j for j in range(1, n+1)])
    submit = set(list(map(int, input().split())))
    
    print(f'#{i}', end=' ')
    print(*sorted(list(students - submit)))