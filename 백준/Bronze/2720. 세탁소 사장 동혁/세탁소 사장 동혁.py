import sys

T = int(sys.stdin.readline())

for i in range(T):
    quarter = 0
    Dime = 0
    Nickel = 0
    Penny = 0

    C = int(sys.stdin.readline())
    
    while C >= 25:
        C -= 25
        quarter += 1
    while C >= 10:
        C -= 10
        Dime += 1
    while C >= 5:
        C -= 5
        Nickel += 1
    while C >= 1:
        C -= 1
        Penny += 1
    print(quarter, Dime, Nickel, Penny)