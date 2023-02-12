x = int(input())
bar_list = [64]

while x != sum(bar_list):
    bar_list = sorted(bar_list, reverse=True)
    half = bar_list.pop() // 2
    if sum(bar_list) + half >= x:
        bar_list.append(half)
    else:
        bar_list.append(half)
        bar_list.append(half)
print(len(bar_list))