import sys

def has_prefix(phone_numbers):
    phone_numbers.sort()
    for i in range(len(phone_numbers) - 1):
        if phone_numbers[i + 1].startswith(phone_numbers[i]):
            return True
    return False

T = int(sys.stdin.readline())

for _ in range(T):
    phone_numbers = []
    n = int(sys.stdin.readline())

    for _ in range(n):
        phone_number = sys.stdin.readline().strip()
        phone_numbers.append(phone_number)

    if has_prefix(phone_numbers):
        result = 'NO'
    else:
        result = 'YES'

    print(result)
