function solution(num_list) {
    var answer = 0;
    var even = '';
    var odd = '';
    for (const i of num_list) {
        if (i % 2 === 0) {
            even += i.toString();
        } else {
            odd += i.toString();
        }
        answer = parseInt(even) + parseInt(odd);
    }
    return answer;
}