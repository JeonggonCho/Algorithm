function solution(num_list) {
    var answer = 0;
    for (const i of num_list) {
        if (i < 0) {
            answer = num_list.indexOf(i);
            return answer;
        }
    } answer = -1;
    return answer;
}