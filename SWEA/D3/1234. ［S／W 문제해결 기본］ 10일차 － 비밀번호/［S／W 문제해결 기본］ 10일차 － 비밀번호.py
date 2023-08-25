for i in range(1, 11):
    n, numbers = input().split()
    numbers = list(numbers)
    stack = []

    while len(numbers):
        stack.append(numbers.pop())
        if len(stack) and len(numbers):
            while True:
                if len(numbers) and len(stack) and numbers[-1] == stack[-1]:
                    numbers.pop()
                    stack.pop()
                else:
                    break
    
    stack.reverse()
    print(f'#{i} {int("".join(stack))}')