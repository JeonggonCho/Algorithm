while(1):
    str_val = input()
    if str_val =='.':
        break
        
    stack = []
    result = True
    
    for el in str_val:
        if el == '(' or el =='[':
            stack.append(el)
        elif el==')':
            if len(stack)==0 or stack[-1]=='[':
                result = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif el==']':
            if len(stack)==0 or stack[-1]=='(':
                result = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if len(stack)==0 and result==True:
        print('yes')
    else:
        print('no')