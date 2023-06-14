function solution(num_list) {
    var answer = [];
    num_list.sort(function(a, b)  {
        return a - b;
    });
    answer = num_list.slice(0, 5);
    return answer;
}