function solution(rank, attendance) {
    var answer = 0;
    var arr = [];
    for (let i = 0; i < rank.length; i++) {
        if (attendance[i] === true) {
            arr.push(rank[i]);
        }
    }
    arr.sort(function(a, b) {
        return a - b;
    });
    answer = 10000 * rank.indexOf(arr[0]) + 100 * rank.indexOf(arr[1]) + rank.indexOf(arr[2]);
    return answer;
}