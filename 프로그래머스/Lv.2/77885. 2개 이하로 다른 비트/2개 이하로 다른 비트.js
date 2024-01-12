function solution(numbers) {
    
    
    function process(cnt) {
        let resultBinaryNum = "10";
        for (let i = 0; i < cnt - 1; i++) {
            resultBinaryNum += "1";
        }
        return resultBinaryNum;
    }
    
    
    var answer = [];
    for (const num of numbers) {
        if (num % 2 === 0) {
            answer.push(num + 1);
        } else {
            let binaryNum = num.toString(2).split("");
            let cnt = 0;
            while (binaryNum[binaryNum.length - 1] === "1") {
                binaryNum.pop();
                cnt++;
            }
            if (binaryNum.length === 0) {
                let result = process(cnt);
                answer.push(parseInt(result, 2));
            } else {
                binaryNum.pop()
                let result = binaryNum.join("") + process(cnt);
                answer.push(parseInt(result, 2));
            }
        }
    }
    return answer;
}