function solution(num_list, n) {
    var answer = [];
    answer = (num_list.slice(n, num_list.length + 1)).concat(num_list.slice(0, n))
    return answer;
}