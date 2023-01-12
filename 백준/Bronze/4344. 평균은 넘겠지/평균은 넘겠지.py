C = int(input())

for i in range(C):
    list1 = list(map(int, input().split()))
    
    N = float(list1[0])
    score = list1[1::]
    average = float(sum(score)) / N
    cnt = 0

    for j in score:
        if j > average:
            cnt += 1
    print('{:.3f}%'.format(round((cnt / len(score) * 100), 3)))