import sys

cnt = {}
char = sys.stdin.readline()

for i in char:
    if ord(i) >= 97 and ord(i) <= 122:
        upper_char = chr(ord(i) - 32)
        if upper_char not in cnt:
            cnt[upper_char] = 1
        else:
            cnt[upper_char] += 1
    elif ord(i) >= 65 and ord(i) <= 90:
        if i not in cnt:
            cnt[i] = 1
        else:
            cnt[i] += 1

max_cnt = max(cnt.values())
max_keys = []

for j in cnt:
    if cnt[j] == max_cnt:
        max_keys.append(j)

if len(max_keys) == 1:
    print(max_keys[0])
else:
    print("?")