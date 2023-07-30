function solution(s) {
    var sArr = s.split("");
    var answer = 0;
    for (let i = 0; i < s.length; i++) {
        let check = collect(sArr);
        if (check === true) {
            answer++;
            var firstChar = sArr.shift();
            sArr.push(firstChar);
        } else {
            var firstChar = sArr.shift();
            sArr.push(firstChar);
        }
    }
    return answer;
}

function collect(char) {
    var arr = [];
    for (const j of char) {
        if (arr.length === 0) {
            arr.push(j);
        } else if (arr[arr.length - 1] === "[" && j === "]") {
            arr.pop();
        } else if (arr[arr.length - 1] === "{" && j === "}") {
            arr.pop();
        } else if (arr[arr.length - 1] === "(" && j === ")") {
            arr.pop();
        } else {
            arr.push(j);
        }
    }
    let isAllowed = (arr.length === 0) ? true : false;
    return isAllowed;
}