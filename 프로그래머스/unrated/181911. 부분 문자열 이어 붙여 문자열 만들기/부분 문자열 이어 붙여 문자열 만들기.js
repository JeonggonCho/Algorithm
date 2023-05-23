function solution(my_strings, parts) {
    var answer = '';
    for (i = 0; i < parts.length; i++) {
        answer += my_strings[i].slice(parts[i][0], parts[i][1]+1);
    }
    return answer;
}