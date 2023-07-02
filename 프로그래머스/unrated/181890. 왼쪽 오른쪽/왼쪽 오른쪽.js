function solution(str_list) {
    var answer = [];
    for (let i = 0; i < str_list.length; i++) {
        if (str_list.at(i) === 'l') {
            answer = str_list.slice(0, i);
            return answer;
        } else if (str_list.at(i) === 'r') {
            answer = str_list.slice(i+1);
            return answer;
        }
    }
    return answer;
}