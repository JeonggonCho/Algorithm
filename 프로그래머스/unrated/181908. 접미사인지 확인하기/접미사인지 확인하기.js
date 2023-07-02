function solution(my_string, is_suffix) {
    var answer = 0;
    while (is_suffix.length !== 0) {
        var char1 = my_string.slice(-1);
        my_string = my_string.slice(0, -1);
        var char2 = is_suffix.slice(-1);
        is_suffix = is_suffix.slice(0, -1);
        if (char1 !== char2) {
            return answer;
        }
    }
    answer = 1;
    return answer;
}