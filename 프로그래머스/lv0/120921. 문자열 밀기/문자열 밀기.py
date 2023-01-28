def solution(A, B):
    answer = 0
    for i in range(len(A)):
        if A == B:
            break
        A = A[-1] + A[0: len(A)-1]
        answer += 1
    else:
        answer = -1
    return answer