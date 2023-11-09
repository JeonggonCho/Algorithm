import sys
import math

def is_conclude(x, y, cx, cy, r): # 출발점 및 도착점을 행성계가 포함하는지 판단하는 함수
    distance = math.sqrt((x - cx) ** 2 + (y - cy) ** 2) # 행성계의 중심점과 출발점 또는 도착점까지의 거리 distance
    if distance > r: # 거리 distance가 행성계 반지름 r보다 크면 포함하지 않아 False리턴, 아니면 포함하므로 True리턴
        return False
    else:
        return True

T = int(sys.stdin.readline()) # 테스트케이스 수 T

for i in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split()) # 출발점, 도착점 좌표 입력받기
    N = int(sys.stdin.readline()) # 행성계 개수 N
    cnt = 0 # 진입/출입 카운드 cnt

    for j in range(N):
        cx, cy, r = map(int, sys.stdin.readline().split()) # 행성계 중심좌표 및 반지름 입력받기
        with_start_point = is_conclude(x1, y1, cx, cy, r) # 출발점이 행성계에 포함되는지 판단
        with_end_point = is_conclude(x2, y2, cx, cy, r) # 도착점이 행성계에 포함되는지 판단

        if with_start_point == True and with_end_point == False: # 출발점, 도착점 중 하나만 포함하는 경우, 진입/출입 +1
            cnt += 1
        elif with_start_point == False and with_end_point == True:
            cnt += 1

    print(cnt) # 최종 진입/출입 수 출력