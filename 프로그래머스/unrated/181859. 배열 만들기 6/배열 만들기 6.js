function solution(arr) {
    var stk = [];
    var i = 0;
    while (i < arr.length) {
        if (stk.length === 0) {
            stk.push(arr[i]);
            i += 1;
        } else if (stk.length !== 0) {
            if (stk.at(-1) === arr[i]) {
                stk.pop();
                i += 1;
            } else {
                stk.push(arr[i]);
                i += 1;
            }
        }
    }
    if (stk.length === 0) {
        return [-1];
    }
    return stk;
}