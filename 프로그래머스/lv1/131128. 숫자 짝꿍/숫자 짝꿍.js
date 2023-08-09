function solution(X, Y) {
    var answer = '';
    var xArr = X.split("").map(Number);
    var yArr = Y.split("").map(Number);
    var yObj = {};
    xArr.sort(function(a, b) {
        return b - a;
    })
    for (const i of yArr) {
        if (yObj[i] === undefined) {
            yObj[i] = 1;
        } else {
            yObj[i]++;
        }
    }
    for (const j of xArr) {
        if (yObj[j] !== undefined && yObj[j] !== 0) {
            answer += j.toString();
            yObj[j]--;
        }
    }
    if (answer.length === 0) {
        return "-1";
    } else if (answer.charAt(0) === "0") {
        return "0";
    } else {
        return answer;
    }
}