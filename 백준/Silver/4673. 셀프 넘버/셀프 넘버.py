def dn(num):
    return num + sum(map(int, list(str(num))))

li = [i for i in range(1, 10001)]

for j in range(1, 10001):
    non_self_num = dn(j)
    if non_self_num in li:
        li.remove(non_self_num)

for k in li:
    print(k)