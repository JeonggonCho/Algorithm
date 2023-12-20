import sys


def is_possible(num, buttons):
    numbers = list(map(int, list(str(num))))
    for i in numbers:
        if i in buttons:
            return False
    else:
        return True


channel = int(sys.stdin.readline())
n = int(sys.stdin.readline())
if n != 0:
    broken_buttons = list(map(int, sys.stdin.readline().split()))
else:
    broken_buttons = []

cnt = 0
down = channel
up = channel
only_updown = abs(channel - 100)

if channel == 100:
    print(0)
elif n == 10:
    print(only_updown)
else:
    if is_possible(channel, broken_buttons):
        total = len(list(map(int, list(str(channel)))))
        if total < only_updown:
            print(total)
        else:
            print(only_updown)
    else:
        while True:
            cnt += 1
            if down >= 1:
                down -= 1
            up += 1
            if is_possible(down, broken_buttons):
                total = len(list(map(int, list(str(down))))) + cnt
                if total < only_updown:
                    print(total)
                else:
                    print(only_updown)
                break
            elif is_possible(up, broken_buttons):
                total = len(list(map(int, list(str(up))))) + cnt
                if total < only_updown:
                    print(total)
                else:
                    print(only_updown)
                break