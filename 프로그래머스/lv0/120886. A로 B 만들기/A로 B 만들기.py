def solution(before, after):
    char_before = {}
    char_after = {}
    for i in before:
        char_before[i] = 0
    for j in before:
        char_before[j] += 1
    for k in after:
        char_after[k] = 0
    for l in after:
        char_after[l] += 1
    if sorted(char_before.items()) == sorted(char_after.items()):
        answer = 1
    else:
        answer = 0
    return answer