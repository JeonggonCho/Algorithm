function solution(survey, choices) {
    let answer = '';
    let types = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0};
    
    for (let i = 0; i < survey.length; i++) {
        const [firstType, lastType] = survey[i].split("");
        
        if (choices[i] === 1) {
            types[firstType] += 3;
        } else if (choices[i] === 2) {
            types[firstType] += 2;
        } else if (choices[i] === 3) {
            types[firstType] += 1;
        } else if (choices[i] === 5) {
            types[lastType] += 1;
        } else if (choices[i] === 6) {
            types[lastType] += 2;
        } else if (choices[i] === 7) {
            types[lastType] += 3;
        }
    };
    
    types["R"] >= types["T"] ? answer += "R" : answer += "T";
    types["C"] >= types["F"] ? answer += "C" : answer += "F";
    types["J"] >= types["M"] ? answer += "J" : answer += "M";
    types["A"] >= types["N"] ? answer += "A" : answer += "N";
    
    return answer;
}