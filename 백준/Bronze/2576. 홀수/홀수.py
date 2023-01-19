numbers = []
num_odd = []

for i in range(7):
    numbers.append(int(input()))

for j in numbers:
    if j % 2 == 1:
        num_odd.append(j)
if len(num_odd) == 0:
    print(-1)
else:
    print(sum(num_odd))
    print(min(num_odd))