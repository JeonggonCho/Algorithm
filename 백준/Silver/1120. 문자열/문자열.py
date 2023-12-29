import sys

def diff(num1, num2):
    answer = 0
    for i in range(len(num1)):
        if num1[i] != num2[i]:
            answer += 1
    return answer


A, B = sys.stdin.readline().strip().split()

if len(A) == len(B):
    result = diff(A, B)
else:
    result = len(A)
    for j in range(0, len(B) - len(A) + 1):
        sliced_B = B[j: j + len(A) + 1]
        difference = diff(A, sliced_B)
        if result >= difference:
            result = difference

print(result)