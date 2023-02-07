import sys

h_list = []
cnt = 1

n = int(sys.stdin.readline())

for i in range(n):
    h = int(sys.stdin.readline())
    h_list.append(h)

max_h = h_list[-1]

while h_list:
    compare = h_list.pop()
    if compare > max_h:
        max_h = compare
        cnt += 1

print(cnt)