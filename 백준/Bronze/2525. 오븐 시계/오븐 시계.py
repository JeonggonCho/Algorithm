H, M = input().split( )
time = input()

if (int(M) + int(time)) < 60:
    print(int(H), (int(M) + int(time)))
else:
    print(((int(H) + ((int(M) + int(time)) // 60)) % 24), (int(M) + int(time)) % 60)