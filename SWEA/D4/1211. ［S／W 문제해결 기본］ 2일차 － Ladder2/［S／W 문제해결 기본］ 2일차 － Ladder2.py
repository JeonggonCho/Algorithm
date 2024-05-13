answers = []

# 사다리에서 이동할 수 있는 오른쪽(dr), 왼쪽(dl), 아래(du)를 딕셔너리로 설정
d = {
    'dr': [0, 1],
    'dl': [0, -1],
    'du': [1, 0]
}

# 테스트 케이스 수 10번 실행
for _ in range(10):
    # 테스트 케이스 번호 입력 받기
    T = int(input())

    # 100 x 100 이차원 배열 생성
    matrix = []
    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)

    # 시작점 인덱스 확인하기
    start_indexes = []
    for k in range(0, 100):
        if matrix[0][k] == 1:
            start_indexes.append(k)

    all_distances = []

    # 각 시작점 순회하며 길이 재기
    for l in start_indexes:
        position = [0, l] # 현재 위치 좌표
        distance = 0 # 이동한 거리
        direction = 'du' # 이동할 방향

        while position[0] != 99:
            position[0] += d[direction][0]
            position[1] += d[direction][1]
            distance += 1

            if direction == 'du' and position[1] < 99 and matrix[position[0]][position[1] + 1] == 1:
                direction = 'dr'
            elif direction == 'du' and position[1] > 0 and matrix[position[0]][position[1] - 1] == 1:
                direction = 'dl'
            elif direction != 'du' and position[0] < 99 and matrix[position[0] + 1][position[1]] == 1:
                direction = 'du'

        all_distances.append(distance)

    # 최소 거리값을 구하고 해당 값과 같은 거리 값을 가지는 시작점 인덱스를 indexes 리스트에 모으고 가장 큰 인덱스 출력하기
    min_distance = min(all_distances)
    indexes = [start_indexes[m] for m, n in enumerate(all_distances) if n == min_distance]
    max_index = max(indexes)

    answers.append(f'#{T} {max_index}')

for o in answers:
    print(o)
