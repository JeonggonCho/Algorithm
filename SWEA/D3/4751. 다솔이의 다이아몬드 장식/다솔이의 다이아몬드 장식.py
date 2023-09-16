T = int(input())

for i in range(1, T+1):
    char = input()
    length = len(char)

    for j in range(length):
        print('..#.', end='')
    print('.', end='\n')

    for k in range(length):
        print('.#.#', end='')
    print('.', end='\n')

    for l in char:
        print(f'#.{l}.', end='')
    print('#', end='\n')

    for k in range(length):
        print('.#.#', end='')
    print('.', end='\n')

    for j in range(length):
        print('..#.', end='')
    print('.', end='\n')