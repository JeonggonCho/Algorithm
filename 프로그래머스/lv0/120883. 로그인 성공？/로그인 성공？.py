def solution(id_pw, db):
    for i in db:
        if id_pw[0] != i[0]:
            answer = 'fail'
        else:
            if id_pw[1] == i[1]:
                answer = 'login'
            else:
                answer = 'wrong pw'
                break
    return answer