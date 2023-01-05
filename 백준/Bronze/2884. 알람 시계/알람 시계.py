H, M = input().split( )

if int(M) >= 45:
    print(int(H), (int(M) - 45))
if int(M) < 45:
    if int(H) == 0:
        print(23, (60-(45-int(M))))
    else:
        print((int(H)-1), (60-(45-int(M))))