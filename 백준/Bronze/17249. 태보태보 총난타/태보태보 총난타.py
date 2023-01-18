char = input()
left_num = 0
right_num =0

for i in char:
    if i == '@':
        left_num += 1
    elif i == '(':
        break
for j in char[::-1]:
    if j == '@':
        right_num += 1
    elif j == ')':
        break
print(left_num, right_num)