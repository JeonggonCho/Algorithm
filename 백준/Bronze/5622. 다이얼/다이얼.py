chars = input()
num_alpha = {}
cnt = 3
time = 0

list_alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
for i in list_alpha:
    num_alpha[i] = cnt
    cnt += 1

for j in list_alpha:
    for k in chars:
        if k in j:
            time += num_alpha[j]
print(time)