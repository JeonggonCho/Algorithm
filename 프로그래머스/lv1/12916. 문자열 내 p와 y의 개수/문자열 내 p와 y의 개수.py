def solution(s):
    p_cnt = (s.lower()).count('p')
    y_cnt = (s.lower()).count('y')
    if p_cnt != y_cnt:
        return False
    else:
        return True