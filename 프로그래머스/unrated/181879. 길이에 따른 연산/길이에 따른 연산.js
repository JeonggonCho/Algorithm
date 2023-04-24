add = function(arr) {
    return arr.reduce((a, b) => a + b);
};

function solution(num_list) {
    var answer = 1;
    if (num_list.length >= 11) {
        answer = num_list.reduce((prev, curr) => prev + curr);
    } else if (num_list.length <= 10) {
        for (const i of num_list) {
            answer *= i;
        }
    }
    return answer;
}