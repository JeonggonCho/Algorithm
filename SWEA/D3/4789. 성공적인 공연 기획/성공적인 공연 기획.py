results = []

T = int(input())

for i in range(1, T+1):
    people = list(map(int, list(input())))
    cnt = people[0]
    need = 0
    for j in range(1, len(people)):
        if people[j] != 0:
            if cnt >= j:
                cnt += people[j]
            else:
                more = j - cnt
                cnt += (more + people[j])
                need += more

    results.append(f'#{i} {need}')

for k in results:
    print(k)