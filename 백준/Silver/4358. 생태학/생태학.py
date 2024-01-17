trees = {}
cnt = 0
tree_list = []

while True:
    try:
        tree = input().strip()
        cnt += 1
        if trees.get(tree):
            trees[tree] += 1
        else:
            trees[tree] = 1
            tree_list.append(tree)
    except EOFError:
        break

tree_list.sort()

for i in tree_list:
    print("%s %.4f" % (i, (trees[i] / cnt * 100)))
