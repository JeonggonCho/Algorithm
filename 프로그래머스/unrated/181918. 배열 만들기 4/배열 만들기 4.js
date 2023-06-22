function solution(arr) {
    var stk = [];
    var i = 0;
    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i]);
            i += 1;
        } else if (stk.length !== 0 && stk.at(-1) < arr[i]) {
            stk.push(arr[i]);
            i += 1;
        } else if (stk.length !== 0 && stk.at(-1) >= arr[i]) {
            stk.pop();
        }
    }
    return stk;
}