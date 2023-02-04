for i in range(1, 11):
    check_list = []
    n = int(input())
    char = list(input())
    
    for j in range(len(char)):
        bracket = char.pop()
        
        if bracket == '(' and check_list[-1] == ')':
            check_list.pop()    
        elif bracket == '{' and check_list[-1] == '}':
            check_list.pop()    
        elif bracket == '[' and check_list[-1] == ']':
            check_list.pop()    
        elif bracket == '<' and check_list[-1] == '>':
            check_list.pop()
        else:
            check_list.append(bracket)

    if len(char) == 0 and len(check_list) == 0:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')