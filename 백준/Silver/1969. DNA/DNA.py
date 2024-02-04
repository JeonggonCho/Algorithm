import sys

def make_dna(list, length):
    new_dna = ''
    hamming_distance = 0
    for j in range(length):
        category = {'A': 0, 'C': 0, 'G': 0, 'T': 0,}
        for k in list:
            category[k[j]] += 1
        result = sorted(category, key=lambda x: (-category[x], x))
        new_dna += result[0]
        del category[result[0]]
        hamming_distance += sum(category.values())
    return (new_dna, hamming_distance)


N, M = map(int, sys.stdin.readline().split())

all_dna = []
for i in range(N):
    dna = sys.stdin.readline()
    all_dna.append(dna)

answers = make_dna(all_dna, M)
print(f'{answers[0]}\n{answers[1]}')