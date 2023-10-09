T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    li1 = set(input().split())
    li2 = set(input().split())
    intersected_chars = li1.intersection(li2)
    print(f'#{i } {len(intersected_chars)}')