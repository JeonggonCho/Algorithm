function solution(x1, x2, x3, x4) {
    var answer = true;
    answer = calc2(calc1(x1, x2), calc1(x3, x4))
    return answer;
}

function calc1(a, b) {
    if (a === true && b === true) {
        return true;
    } else if (a === true && b === false) {
        return true;
    } else if (a === false && b === true) {
        return true;
    } else if (a === false && b === false) {
        return false;
    }
}

function calc2(c, d) {
    if (c === true && d === true) {
        return true;
    } else if (c === true && d === false) {
        return false;
    } else if (c === false && d === true) {
        return false;
    } else if (c === false && d === false) {
        return false;
    }
}