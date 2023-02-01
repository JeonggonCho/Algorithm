import sys
from collections import deque, Counter

T = int(sys.stdin.readline().strip()) # 테스트케이스 수 입력받기


for i in range(T):
    m, n = map(int, sys.stdin.readline().split()) # 행(m)과 열(n)의 개수를 입력받기

    transposed_matrix = [[0] * m for j in range(n)] # 전치를 담을 이차원 리스트 형성하기
    cnt = 0 # 박스가 움직인 거리를 담을 변수 초기화 

    matrix = [list(map(int, sys.stdin.readline().split())) for k in range(m)] #행(m) 만큼 반복해서 박스패턴 입력받기

    for l in range(n):
        for o in range(m):
            transposed_matrix[l][o] = matrix[o][l] # 입력받은 박스패턴 전치 시키기
    

    for p in range(n): # 행을 하나씩 순회
        box_list = deque(transposed_matrix[p]) # 행을 deque로 변환

        for q in range(len(box_list)): # 행의 열 개수만큼 순회
            box = box_list.popleft() # popleft로 하나씩 꺼내기
            if box == 1: # 꺼낸 숫자가 1인 경우,
                check = Counter(box_list) # 남은 박스패턴의 '1'의 개수와 '0'의 개수를 check 딕셔너리로 받기
                for key, value in check.items(): # 딕셔너리에서 숫자(키)와 개수(값)을 순회
                    if key == 0: # 숫자가 0인 키의 개수(값)을 cnt에 누적
                        cnt += value
    
    print(cnt) # 움직인 카운팅을 출력