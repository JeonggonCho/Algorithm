function solution(arr, delete_list) {
    var answer = [];
    for (const i of arr) {
        if (! delete_list.includes(i)) {
            answer.push(i)
        }
    }
    return answer;
}