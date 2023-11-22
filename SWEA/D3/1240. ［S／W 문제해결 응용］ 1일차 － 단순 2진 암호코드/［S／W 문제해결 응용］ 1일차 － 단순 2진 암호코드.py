def is_password(str):
    num1, num2, num3 = 0, 0, 0

    for _ in range(8):
        num = int(str[_])
        num3 += num
        if (_ + 1) % 2 == 1:
            num1 += num
        else:
            num2 += num

    if (num1 * 3 + num2) % 10 == 0:
        return num3
    else:
        return 0


code_rule = {
    0: [3, 2, 1, 1],
    1: [2, 2, 2, 1],
    2: [2, 1, 2, 2],
    3: [1, 4, 1, 1],
    4: [1, 1, 3, 2],
    5: [1, 2, 3, 1],
    6: [1, 1, 1, 4],
    7: [1, 3, 1, 2],
    8: [1, 2, 1, 3],
    9: [3, 1, 1, 2],
}


T = int(input())

for i in range(1, T+1):
    n, m = map(int, input().split())
    code_line = []
    for j in range(n):
        code = list(input())
        if '1' in code and code_line == []:
            code_line = code

    while code_line[-1] == '0':
        code_line.pop()

    number = ''
    for k in range(8):
        one_code = code_line[-7:]
        one_barcode = {}
        seq = 1

        for l in range(7):
            if len(one_barcode) == 0:
                one_barcode[seq] = 1
            elif one_code[l] == one_code[l-1]:
                one_barcode[seq] += 1
            else:
                seq += 1
                one_barcode[seq] = 1

        for m in range(7):
            code_line.pop()

        for n in range(10):
            if code_rule[n] == list(one_barcode.values()):
                number = str(n) + number
                break

    result = is_password(number)

    print(f'#{i} {result}')