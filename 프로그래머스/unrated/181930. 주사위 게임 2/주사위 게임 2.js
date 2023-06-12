function solution(a, b, c) {
    var answer = 0;
    var arr = [];
    arr.push(a);
    arr.push(b);
    arr.push(c);
    
    const setArr = Array.from(new Set(arr));
    
    if (setArr.length === 3) {
        answer = a + b + c;
    } else if (setArr.length === 2) {
        answer = (a + b + c) * (a ** 2 + b ** 2 + c ** 2);
    } else if (setArr.length === 1) {
        answer = (3 * a) * (3 * (a ** 2)) * (3 * (a ** 3));
    }
    return answer;
}