function solution(my_string, n) {
    var answer = '';
    answer = my_string.slice(my_string.length - n);
    return answer;
}