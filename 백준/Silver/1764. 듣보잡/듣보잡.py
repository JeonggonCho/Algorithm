import sys

n, m = map(int, sys.stdin.readline().split())
set1 = set()
set2 = set()

for i in range(n):
    name1 = sys.stdin.readline().strip()
    set1.add(name1)

for j in range(m):
    name2 = sys.stdin.readline().strip()
    set2.add(name2)

intersected_set = sorted(set1.intersection(set2))

print(len(intersected_set))
for k in intersected_set:
    print(k)