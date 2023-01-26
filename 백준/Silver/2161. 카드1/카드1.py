import sys

N = int(sys.stdin.readline())
num_list =[]

for i in range(1, N+1):
    num_list.append(i)
    
while len(num_list) != 1:
    print(num_list.pop(0), end=' ')
    num_list.append(num_list.pop(0))
print(num_list[0])