function solution(number, limit, power) {
    var answer = 0;
    for (let j = 1; j < number + 1; j++) {
        var cnt = div(j);
        if (cnt <= limit) {
            answer += cnt;
        } else {
            answer += power;
        }
    }
    return answer;
}

// 약수 개수 구하는 함수
function div(num) {
    var cnt = 0;
    for (let i = 1; i <= num / 2; i++) {
        if (num % i === 0) {
            cnt++;
        }
    }
    return cnt + 1;
}