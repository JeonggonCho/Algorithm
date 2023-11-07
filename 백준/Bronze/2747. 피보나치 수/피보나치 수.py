import sys

def fibonacci(numbers):
    numbers.append(numbers[-2] + numbers[-1])

numbers = [0, 1]

n = int(sys.stdin.readline())

if n == 0:
    print(numbers[0])
elif n == 1:
    print(numbers[1])
else:
    while len(numbers) != n + 1:
        fibonacci(numbers)
    print(numbers[-1])