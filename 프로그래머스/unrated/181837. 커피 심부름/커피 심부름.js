function solution(order) {
    var answer = 0;
    for (const i of order) {
        if (i.includes('americano')) {
            answer += 4500;
        } else if (i.includes('cafelatte')) {
            answer += 5000;
        } else if (i.includes('anything')) {
            answer += 4500;
        }
    }
    return answer;
}