import sys

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

T = int(sys.stdin.readline())

for i in range(T):
    nums = list(map(int, sys.stdin.readline().split()))
    result = lcm(nums[0], nums[1])
    print(result)
