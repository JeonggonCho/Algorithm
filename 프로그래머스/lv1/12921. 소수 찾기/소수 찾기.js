// 초기 시도 코드

// function solution(n) {
//     var answer = 0;
//     for (let i = 2; i <= n; i++) {
//         var divisorCnt = 0; 
//         for (let j = 2; j <= Math.sqrt(i); j++) {
//             if (i % j === 0) {
//                 divisorCnt += 1;
//                 break;
//             }
//         }
//         if (divisorCnt === 0) {
//             answer += 1;
//         }
//     }
//     return answer;
// }


// 에라토스테네스의 체 알고리즘을 사용

function solution(n) {
  const sieve = new Array(n + 1).fill(true); // 모두 true로 처리된 n길이의 배열 형성
  sieve.splice(0, 2, false, false); // 0, 1은 소수가 아니므로 false로 치환
    
    for (let i = 2; i <= Math.sqrt(n); i++) { // 2부터 n의 제곱근까지 확인
        if (sieve[i] === true) { // 해당 인덱스가 소수일 경우, 소수의 배수는 합성수이다.
            for (let j = i * i; j <= n; j += i) {
                sieve[j] = false; // 소수의 배수들을 false로 치환
            }
        }
    }
    const answer = sieve.filter((element) => element === true).length; // true 개수 세기
    return answer;
}