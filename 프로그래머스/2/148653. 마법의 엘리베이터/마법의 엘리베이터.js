function solution(storey) {
    let answer = 0;
    
    while (storey > 0) {
        let num = storey % 10;
        storey = Math.floor(storey / 10);
        
        if (num > 5) {
            answer += (10 - num);
            storey++;
        } else if (num < 5) {
            answer += num;
        } else if (storey % 10 >= 5) {
            answer += 5;
            storey++;
        } else {
            answer += 5;
        }
    }
    return answer;
}
