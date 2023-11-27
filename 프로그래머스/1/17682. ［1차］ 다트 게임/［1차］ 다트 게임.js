function solution(dartResult) {
    const numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
    const bonusStrings = ["S", "D", "T"];
    const optionStrings = ["*", "#"];
    
    let scores = [];
    let bonus = [];
    let options = [];
    
    // 점수와 보너스 및 옵션 분리
    let getScore = "";
    
    for (let i = 0; i < dartResult.length; i++) {
        let char = dartResult[i]
        if (numbers.includes(char)) {
            getScore += dartResult[i];
        } else if (bonusStrings.includes(char)) {
            scores.push(parseInt(getScore));
            getScore = "";
            bonus.push(char);
            if (numbers.includes(dartResult[i + 1])) {
                options.push("");
            }
        } else if (optionStrings.includes(char)) {
            options.push(char);
        }
    }
    
    // 점수에 보너스 적용
    for (let j = 0; j < bonus.length; j++) {
        if (bonus[j] === "S") {
            scores[j] **= 1;
        } else if (bonus[j] === "D") {
            scores[j] **= 2;
        } else if (bonus[j] === "T") {
            scores[j] **= 3;
        }
    }
    
    // 점수에 옵션 적용
    for (let k = 0; k < options.length; k++) {
        if (options[k] === "*") {
            if (k > 0) {
                scores[k] *= 2;
                scores[k - 1] *= 2;
            } else {
                scores[k] *= 2;
            }
        } else if (options[k] === "#") {
            scores[k] *= (-1);
        }
    }
    
    // 점수 총합
    let answer = 0;
    
    for (let l of scores) {
        answer += l;
    }
    
    return answer;
}