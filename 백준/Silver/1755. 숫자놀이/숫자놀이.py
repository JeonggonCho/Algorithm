import sys

numbers = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
}

M, N = map(int, sys.stdin.readline().split())

dict = {}
for i in range(M, N + 1):
    convert = []
    for j in list(str(i)):
        convert.append(numbers[j])
    dict[i] = " ".join(convert)

answers = list(map(str, sorted(dict, key=lambda x: dict[x])))

for i in range(0, len(answers), 10):
    print(" ".join(answers[i:i + 10]))