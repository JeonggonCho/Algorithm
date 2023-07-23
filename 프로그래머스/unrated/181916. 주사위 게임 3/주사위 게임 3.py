def solution(a, b, c, d):
    answer = 0
    dic = {}
    dice_list = [a, b, c, d]
    for i in dice_list:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    # 모두 같은 값일 경우
    if len(dic) == 1:
        p = list(dic.keys())[0]
        return 1111 * p
    # 세 개가 같은 값이고 나머지 하나가 다른 값일 경우
    elif len(dic) == 2 and sorted(list(dic.values())) == [1, 3]:
        p = sorted(dic, key=lambda x: dic[x])[1]
        q = sorted(dic, key=lambda x: dic[x])[0]
        return (10 * p + q) ** 2
    # 두 개씩 같은 값일 경우
    elif len(dic) == 2 and list(dic.values()) == [2, 2]:
        p = list(dic.keys())[0]
        q = list(dic.keys())[1]
        return (p + q) * abs(p - q)
    # 두 개가 같은 값이고 나머지가 각각 다른 값일 경우
    elif len(dic) == 3:
        p = sorted(dic, key=lambda x: dic[x])[1]
        q = sorted(dic, key=lambda x: dic[x])[0]
        return p * q
    # 네 개의 값이 모두 다른 경우
    elif len(dic) == 4:
        return min(sorted(dice_list))