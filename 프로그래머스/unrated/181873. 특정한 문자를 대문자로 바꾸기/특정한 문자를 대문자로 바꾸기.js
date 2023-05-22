function solution(my_string, alp) {
    var answer = '';
    for (i = 0; i < my_string.length; i++) {
        var char = my_string.charAt(i);
        if (char === alp) {
            answer += char.toUpperCase();
        } else {
            answer += char;
        }
    }
    return answer;
}