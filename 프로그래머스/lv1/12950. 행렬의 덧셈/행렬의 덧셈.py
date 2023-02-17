def solution(arr1, arr2):
    answer = [[] for i in range(len(arr1))]
    for j in range(len(arr1)):
        for k in range(len(arr1[0])):
            answer[j].append(arr1[j][k] + arr2[j][k])
    return answer