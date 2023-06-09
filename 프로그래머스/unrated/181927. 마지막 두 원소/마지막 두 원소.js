function solution(num_list) {
    var answer = [];
    var lastElement = num_list.at(-1);
    var preElement = num_list.at(-2);
    if (lastElement > preElement) {
        num_list.push(lastElement - preElement);
    } else {
        num_list.push(lastElement * 2);
    }
    answer = num_list;
    return answer;
}