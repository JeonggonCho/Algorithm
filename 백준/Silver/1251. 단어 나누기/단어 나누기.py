import sys

char = sys.stdin.readline().strip()
char_list = []

for i in range(1, len(char)-1):
    for j in range(i+1, len(char)):
        new_char = char[:i][::-1] + char[i:j][::-1] + char[j:][::-1]
        char_list.append(new_char)

print(sorted(char_list)[0])