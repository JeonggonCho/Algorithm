def solution(bin1, bin2):
    answer = ''
    a = list(bin1)
    b = list(bin2)
    num3 = 0
    
    for i in range(max(len(bin1), len(bin2))):
        if a:
            num1 = int(a.pop())
        else:
            num1 = 0
        if b:
            num2 = int(b.pop())
        else:
            num2 = 0
            
        if num1 + num2 + num3 == 1:
            answer += '1'
            num3 = 0
        elif num1 + num2 + num3 == 2: 
            answer += '0'
            num3 = 1
        elif num1 + num2 + num3 == 3:
            answer += '1'
            num3 = 1
        else:
            answer += '0'
    answer += str(num3)
    answer = str(int(answer[::-1]))
    return answer