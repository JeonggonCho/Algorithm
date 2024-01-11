limit = 1000000
prime_numbers = []
is_prime = [True] * (limit + 1)

for num in range(2, int(limit**0.5) + 1):
    if is_prime[num]:
        prime_numbers.append(num)
        for multiple in range(num * num, limit + 1, num):
            is_prime[multiple] = False

for num in range(int(limit**0.5) + 1, limit + 1):
    if is_prime[num]:
        prime_numbers.append(num)

print(" ".join(map(str, prime_numbers)))
