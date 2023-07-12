function solution(n) {
    var arr = [0, 1];
    while (arr.length < n + 1) {
        arr.push(arr.at(-2) % 1234567 + arr.at(-1) % 1234567);
    }
    var answer = arr.at(-1) % 1234567;
    return answer;
}