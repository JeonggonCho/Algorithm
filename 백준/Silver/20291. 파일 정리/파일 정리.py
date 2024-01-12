import sys

N = int(sys.stdin.readline())

files = {}
for i in range(N):
    file = sys.stdin.readline().strip().split(".")
    if file[1] not in files:
        files[file[1]] = 1
    else:
        files[file[1]] += 1

sorted_files = sorted(files, key=lambda x: (x, files[x]))
for j in sorted_files:
    print(j, files[j])