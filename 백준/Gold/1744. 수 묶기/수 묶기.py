import sys

n = int(sys.stdin.readline())

positive_seq = []
negative_seq = []
zero = []
for i in range(n):
    number = int(sys.stdin.readline())
    if number > 0:
        positive_seq.append(number)
    elif number == 0:
        zero.append(number)
    else:
        negative_seq.append(number)

positive_seq.sort()
negative_seq.sort(reverse=True)

result = 0
while len(positive_seq) > 1:
    a, b = positive_seq[-1], positive_seq[-2]
    if a == 1 or b == 1:
        result += (a + b)
    else:
        result += (a * b)
    for _ in range(2):
        positive_seq.pop()
while len(negative_seq) > 1:
    c, d = negative_seq[-1], negative_seq[-2]
    result += (c * d)
    for _ in range(2):
        negative_seq.pop()
while len(zero) > 1:
    e = zero.pop()

if zero:
    if positive_seq:
        result += positive_seq[0]
else:
    result += (sum(positive_seq) + sum(negative_seq))

print(result)