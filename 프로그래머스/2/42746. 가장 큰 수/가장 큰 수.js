function solution(numbers) {
    const arr = numbers.map((x) => x.toString());
    arr.sort().reverse();
    arr.sort(function(a, b) {
        if (a.charAt(0) !== b.charAt(0)) {
            return 1;
        } else {
            let result = (parseInt(a + b) > parseInt(b + a)) ? -1 : 1;
            return result;
        }
    });
    let answer = arr.join('');
    while (answer.charAt(0) === '0') {
        answer = answer.slice(1, answer.length - 1);
    }
    answer = (answer === '') ? '0' : answer;
    return answer;
}