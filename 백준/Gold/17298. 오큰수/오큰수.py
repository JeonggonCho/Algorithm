import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

result = [-1] * n  # 결과를 저장할 리스트 초기화
stack = []         # 인덱스를 저장할 스택

for i in range(n):
    while stack and numbers[stack[-1]] < numbers[i]:
        # 현재 숫자보다 큰 숫자가 나올 때까지 스택에서 pop하며 결과 갱신
        result[stack.pop()] = numbers[i]
    stack.append(i)  # 현재 숫자의 인덱스를 스택에 추가

print(*result)
