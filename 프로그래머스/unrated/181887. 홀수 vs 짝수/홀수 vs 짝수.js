function solution(num_list) {
    var answer = 0;
    var even_list = [];
    var odd_list = [];
    var even = 0;
    var odd = 0;
    even_list = num_list
        .filter((_, i) => i % 2 === 0)
        .map((num) => num);
    odd_list = num_list
        .filter((_, i) => i % 2 !== 0)
        .map((num) => num);
    for (const i of even_list) {
        even += i;
    }
    for (const j of odd_list) {
        odd += j;
    }
    if (even >= odd) {
        answer = even;
    } else {
        answer = odd;
    }
    return answer;
}


  