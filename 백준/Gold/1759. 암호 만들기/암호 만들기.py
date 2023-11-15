import sys
from itertools import combinations

vowel = ["a", "e", "i", "o", "u"]

consonant = [chr(i) for i in range(97, 123)]
for j in vowel:
    consonant.remove(j)

def is_password(char):
    vowel_cnt = 0
    consonant_cnt = 0
    for m in char:
        if m in vowel:
            vowel_cnt += 1
        elif m in consonant:
            consonant_cnt += 1
    if vowel_cnt == 0 or consonant_cnt <= 1:
        return False
    else:
        return True


L, C = map(int, sys.stdin.readline().split())
alpha = sys.stdin.readline().split()

possible = sorted([''.join(sorted(k)) for k in combinations(alpha, L)])

for l in possible:
    if is_password(l):
        print(l)