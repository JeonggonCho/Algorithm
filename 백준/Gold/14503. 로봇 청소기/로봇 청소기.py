import sys

direct = {
    0:[-1, 0], # 북
    1:[0, 1], # 동
    2:[1, 0], # 남
    3:[0, -1] # 서
}

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())

room = []
for i in range(N):
    room_condition = list(map(int, sys.stdin.readline().split()))
    room.append(room_condition)

room[r][c] = 2 # 청소된 상태 2로 체크
cnt = 1

while True:
    if all((room[r + direct[j][0]][c + direct[j][1]] == 2 or room[r + direct[j][0]][c + direct[j][1]] == 1) for j in range(4)):
        reversed_d = (d + 2) % 4
        if room[r + direct[reversed_d][0]][c + direct[reversed_d][1]] != 1:
            r += direct[reversed_d][0]
            c += direct[reversed_d][1]
        else:
            break
    else:
        for k in range(4):
            d = (d + 3) % 4
            if room[r + direct[d][0]][c + direct[d][1]] == 0:
                room[r + direct[d][0]][c + direct[d][1]] = 2
                r += direct[d][0]
                c += direct[d][1]
                cnt += 1
                break

print(cnt)