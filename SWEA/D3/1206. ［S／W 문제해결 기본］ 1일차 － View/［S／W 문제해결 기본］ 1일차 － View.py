for i in range(1, 11):
    N = int(input())
    result = 0
    height_list = list(map(int, input().split()))
    
    for k in range(2, len(height_list)-2):
        height = height_list[k]
        surround = sorted([height_list[k-2], height_list[k-1], height_list[k+1], height_list[k+2]])
        
        if surround[-1] >= height:
            continue
        else:
            result += (height - surround[-1])
    
    print(f'#{i} {result}')