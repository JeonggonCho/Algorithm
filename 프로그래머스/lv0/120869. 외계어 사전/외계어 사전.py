def solution(spell, dic):
    answer = 0
    spell_list = []
    for i in dic:
        for j in spell:
            if j in i:
                spell_list.append(j)
        if len(spell_list) == len(spell):
            answer = 1
            break
        else:
            spell_list =[]
    else:
        answer = 2
    return answer