import sys

n = int(sys.stdin.readline())
size_dict = {}
ranking = []

for i in range(1, n+1):
    w, h = map(int, sys.stdin.readline().split())
    size_dict[i] = w, h

for j in size_dict:
    cnt = 1
    for k in size_dict:
        if j != k:
            j_weight = size_dict.get(j)[0]
            j_height = size_dict.get(j)[1]
            k_weight = size_dict.get(k)[0]
            k_height = size_dict.get(k)[1]

            if j_weight < k_weight and j_height < k_height:
                cnt += 1
    ranking.append(cnt)

print(*ranking)