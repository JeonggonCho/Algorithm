T = int(input())

for i in range(1, T+1):
    char = input()
    a = char.count('()')
    b = char.count('|)')
    c = char.count('(|')
    print(f'#{i} {a + b + c}')