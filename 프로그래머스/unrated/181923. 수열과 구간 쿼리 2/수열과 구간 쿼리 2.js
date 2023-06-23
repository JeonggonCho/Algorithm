function solution(arr, queries) {
    var answer = [];
    for (const query of queries) {
        var selectedNum = [];
        for (i = 0; i < arr.length; i++) {
            if (query[0] <= i && i <= query[1] && arr[i] > query[2]) {
                selectedNum.push(arr[i]);
            }
        }
        if (selectedNum.length !== 0) {
           answer.push(Math.min(...selectedNum)); 
        } else {
            answer.push(-1);
        }
        
    }
    return answer;
}