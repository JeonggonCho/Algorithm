import sys

n, m = map(int, sys.stdin.readline().split())

dict = {}
for i in range(n):
    url, password = sys.stdin.readline().strip().split()
    dict[url] = password

for j in range(m):
    find_password = sys.stdin.readline().strip()
    print(dict[find_password])