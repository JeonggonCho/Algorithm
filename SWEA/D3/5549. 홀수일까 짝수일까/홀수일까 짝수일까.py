odd = [1, 3, 5, 7, 9]
even = [0, 2, 4, 6, 8]

T = int(input())

for i in range(1, T+1):
    num = input()
    if int(num[-1]) in odd:
        print(f'#{i} Odd')
    elif int(num[-1]) in even:
        print(f'#{i} Even')