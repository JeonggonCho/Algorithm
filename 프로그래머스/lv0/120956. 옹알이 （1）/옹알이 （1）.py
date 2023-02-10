def solution(babbling):
    answer = 0
    bab = ''
    say = ['aya', 'ye', 'woo', 'ma']
    
    for i in babbling:
        for j in i:
            bab += j
            if bab in say:
                i = i.replace(bab,'')
                bab = ''
        if len(i) == 0:
            answer += 1
        else:
            bab = ''
            
    return answer