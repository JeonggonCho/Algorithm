def solution(wallet, bill):
    answer = 0
    while True:
        if (wallet[0] >= bill[0] and wallet[1] >= bill[1]) or (wallet[0] >= bill[1] and wallet[1] >= bill[0]):
            break
        elif bill[0] > bill[1]:
            bill[0] = bill[0] // 2
            answer += 1
        else:
            bill[1] = bill[1] // 2
            answer += 1
    return answer