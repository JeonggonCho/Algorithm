T = int(input())

for i in range(1, T + 1):
    N = int(input())
    velocity = 0
    distance = 0
    for j in range(N):
        command = input()
        if len(command) == 1:
            distance += velocity * 1
        else:
            control, speed = map(int, command.split())
            if control == 1:
                velocity += speed
                distance += velocity * 1
            elif control == 2:
                if velocity < speed:
                    velocity = 0
                else:
                    velocity -= speed
                    distance += velocity * 1

    print(f'#{i} {distance}')