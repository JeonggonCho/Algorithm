def solution(price):
    if price >= 500000:
        answer = int(price * 0.8)
    elif 500000 > price >= 300000:
        answer = int(price * 0.9)
    elif 300000 > price >= 100000:
        answer = int(price * 0.95)
    else:
        answer = price
    return answer