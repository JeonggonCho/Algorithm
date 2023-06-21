function solution(arr, flag) {
    var answer = [];
    for (i = 0; i < arr.length; i++) {
        if (flag[i] === true) {
            for (j = 0; j < arr[i] * 2; j++) {
                answer.push(arr[i]);
            }
        } else {
            for (k = 0; k < arr[i]; k++) {
                answer.pop();
            }
        }
    }
    return answer;
}