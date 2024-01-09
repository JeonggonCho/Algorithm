function solution(records) {
    let answers = [];
    let temp = new Array;
    const users = new Object;
    const behavior = {
        "Enter": "님이 들어왔습니다.",
        "Leave": "님이 나갔습니다.",
    };
    for (const record of records) {
        let char = record.split(' ');
        if (char[0] === "Enter") {
            users[char[1]] = char[2];
            temp.push([char[1], char[0]]);
        } else if (char[0] === "Leave") {
            temp.push([char[1], char[0]]);
        } else if (char[0] === "Change") {
            users[char[1]] = char[2];
        }
    }
    temp.forEach((result) => {
        let answer = users[result[0]] + behavior[result[1]];
        answers.push(answer);
    });
    return answers;
}