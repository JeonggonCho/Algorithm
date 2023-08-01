function solution(n, k) {
    var answer = 0;
    var changedNum = n.toString(k);
    var arr = [];
    var splitNum = "";
    for (let i = 0; i < changedNum.length; i++) {
        if (changedNum[i] !== "0") {
            splitNum += changedNum[i];
        } else if (changedNum[i] === "0" && splitNum.length !== 0) {
            arr.push(Number(splitNum));
            splitNum = "";
        }
    }
    if (splitNum.length !== 0) {
        arr.push(Number(splitNum));
    }
    
    for (const j of arr) {
        if (j !== 1) {
            var check = true;
            for (let k = 2; k * k <= j; k++) {
                if (j % k === 0) {
                    check = false;
                    break;
                }
            }
            if (check === true) {
                answer++;
            }
        }
    }
    return answer;
}