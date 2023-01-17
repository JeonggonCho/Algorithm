N = int(input())
num_list = []

for i in range(N):
    num_list.append(int(input()))

for j in sorted(num_list):
    print(j)