import sys

n, k = map(int, sys.stdin.readline().split())
num1 = 1
num2 = 1
num3 = 1

for i in range(1, n+1):
    num1 *= i
for j in range(1, k+1):
    num2 *= j
for k in range(1, n-k+1):
    num3 *= k

binomial = (num1 // (num2 * num3)) % 10007
print(binomial)