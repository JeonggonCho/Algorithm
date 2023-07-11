function solution(a, b, n) {
    var answer = 0;
    while (n >= a) {
        var givenCnt = Math.floor(n / a) * b;
        var remainCnt = n % a;
        answer += givenCnt;
        n = givenCnt + remainCnt;
    }
    return answer;
}