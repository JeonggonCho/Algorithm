import sys

num = int(sys.stdin.readline())

books = {}
for i in range(num):
    book = sys.stdin.readline().strip()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1

max_values = max(list(books.values()))

li = []
for j in books:
    if books[j] == max_values:
        li.append(j)

li.sort()

print(li[0])