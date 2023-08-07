function solution(babbling) {
    var answer = 0;
    const words = ["aya", "ye", "woo", "ma"];
    for (const i of babbling) {
        var char = "";
        var records = [];
        for (const j of i) {
            char += j;
            if (words.includes(char) && records[records.length - 1] !== char) {
                records.push(char);
                char = "";
            }
        }
        if (char.length === 0) {
            answer++;
        }
    }
    return answer;
}