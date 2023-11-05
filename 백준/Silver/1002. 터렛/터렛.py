import sys
import math

results = []

T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    if distance == 0 and r1 == r2: # 두 원이 같은 경우
        results.append(-1)
    elif distance == 0 and r1 != r2: # 두 원의 중심이 같고 반지름이 다른 경우
        results.append(0)
    elif distance != 0 and abs(r1 - r2) < distance < r1 + r2: # 두 원이 두 점에서 만나는 경우
        results.append(2)
    elif distance != 0 and distance == r1 + r2: # 두 원이 외접하는 경우
        results.append(1)
    elif distance != 0 and distance > r1 + r2: # 두 원이 따로 떨어져서 안 만나는 경우
        results.append(0)
    elif distance != 0 and distance < abs(r1- r2): # 한 원이 다른 원을 포함하나, 중심이 다른 경우
        results.append(0)
    elif distance != 0 and distance == abs(r1 - r2): # 두 원이 내접하는 경우
        results.append(1)

for j in results:
    print(j)