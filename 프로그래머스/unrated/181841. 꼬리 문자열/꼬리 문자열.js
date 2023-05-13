function solution(str_list, ex) {
    var answer = '';
    for (const i of str_list) {
        if (!i.includes(ex)) {
            answer += i;
        }
    }
    return answer;
}