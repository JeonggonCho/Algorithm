function solution(my_string, is_prefix) {
    var answer = 0;
    while (is_prefix.length !== 0) {
        var char1 = my_string.slice(0, 1);
        my_string = my_string.slice(1);
        var char2 = is_prefix.slice(0, 1);
        is_prefix = is_prefix.slice(1);
        if (char1 !== char2) {
            return answer;
        }
    }
    answer = 1;
    return answer;
}