def check(u, v, d, park): # 체크 시작점(u,v), 돗자리 길이 d
    for j in range(v, v + d):
        for k in range(u, u + d):
            if park[j][k] != "-1": # 깔 수 없으면 False 리턴
                return False
    return True # 깔 수 있는 경우 True 리턴

def solution(mats, park):
    answer = 0
    mats = sorted(mats, reverse = True) # 큰 돗자리부터 정렬
    
    # 돗자리가 공원크기보다 커서 돗자리를 깔 수 없는 경우, 얼리 리턴
    if mats[-1] > len(park) or mats[-1] > len(park[0]):
        return -1
    
    # 돗자리 종류 하나씩 비교 (완전탐색)
    for i in mats:
        for l in range(len(park[0]) - i + 1):
            for m in range(len(park) - i + 1):
                if check(l, m, i, park): # 돗자리 펴는게 가능하면 해당 돗자리 크기 리턴
                    return i
                
    # 모든 돗자리를 깔 수 없는 경우 -1 리턴
    return -1