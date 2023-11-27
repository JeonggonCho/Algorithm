function solution(word) {
    let words = ["A", "E", "I", "O", "U"];
    let temp1 = words;
    let temp2 = words;
    
    for (let i = 0; i < 4; i++) {
        let arr = [];
        for (let j of temp1) {
            for (let k of temp2) {
                arr.push(j + k);
            }
        }
        words = words.concat(arr);
        temp1 = arr;
    }
    const sortedWords = words.sort();
    const answer = sortedWords.indexOf(word) + 1;
    return answer;
}