def solution(quiz):
    answer = []
    for i in quiz:
        math_list = list(i.split())
        if math_list[1] == '-':
            if int(math_list[0]) - int(math_list[2]) == int(math_list[4]):
                answer.append("O")
            else:
                answer.append("X")
        elif math_list[1] == '+':
            if int(math_list[0]) + int(math_list[2]) == int(math_list[4]):
                answer.append("O")
            else:
                answer.append("X")
    return answer