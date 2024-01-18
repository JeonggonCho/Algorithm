import sys

N = int(sys.stdin.readline())

sorted_cards = {}
cards = list(map(int, sys.stdin.readline().split()))
for i in cards:
    sorted_cards[i] = sorted_cards.get(i, 0) + 1

M = int(sys.stdin.readline())

targets = list(map(int, sys.stdin.readline().split()))

answers = []
for j in targets:
    target = sorted_cards.get(j, 0)
    answers.append(str(target))

print(' '.join(answers))