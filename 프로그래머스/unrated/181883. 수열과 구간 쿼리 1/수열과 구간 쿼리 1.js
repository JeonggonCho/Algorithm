function solution(arr, queries) {
    var answer = [];
    for (const i of queries) {
        for (j = i[0]; j < i[1]+1; j++) {
            arr[j] = arr[j] + 1;
        }
    }
    answer = arr;
    return answer;
}