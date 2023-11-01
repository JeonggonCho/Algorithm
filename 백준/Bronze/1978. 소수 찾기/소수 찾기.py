import sys

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

cnt = 0

for j in nums:
    if is_prime(j) and j != 1:
        cnt += 1

print(cnt)