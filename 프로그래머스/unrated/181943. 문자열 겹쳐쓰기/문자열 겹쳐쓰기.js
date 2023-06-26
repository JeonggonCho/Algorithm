function solution(my_string, overwrite_string, s) {
    var answer = '';
    answer += my_string.slice(0, s);
    answer += overwrite_string;
    answer += my_string.slice(s+overwrite_string.length);
    return answer;
}