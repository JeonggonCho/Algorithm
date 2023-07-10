function solution(arr, query) {
    var answer = [];
    for (let i = 0; i < query.length; i++) {
        if (i % 2 === 0) {
            answer = arr.slice(0, query[i] + 1);
        } else {
            answer = arr.slice(query[i]);
        }
        arr = answer;
    }
    return answer;
}