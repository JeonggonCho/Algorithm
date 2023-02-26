import sys

num_list = []

N, P = map(int, sys.stdin.readline().split())

a = N

while True:
    b = a * N % P
    if b not in num_list:
        num_list.append(b)
    else:
        b_position = num_list.index(b)
        answer = num_list[b_position::]
        break
    a = b

print(len(answer))