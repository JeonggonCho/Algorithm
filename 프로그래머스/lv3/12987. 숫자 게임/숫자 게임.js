function solution(A, B) {
    var answer = 0;
    A.sort((a, b) => a - b);
    B.sort((a, b) => a - b);
    
    let j = 0;
    for (let i = 0; i < A.length; i++) {
        while (j < B.length && B[j] <= A[i]) {
            j++;
        }
        if (j < B.length && A[i] < B[j]) {
            answer++;
            j++;
        }
    }
    
    return answer;
}
