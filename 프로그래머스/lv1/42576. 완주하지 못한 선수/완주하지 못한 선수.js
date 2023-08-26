function solution(participant, completion) {
    var answer = '';
    participant.sort();
    completion.sort();
    const len = participant.length;
    for (let i = 0; i < len; i++) {
        var human1 = participant.pop();
        var human2 = completion.pop();
        if (human1 !== human2) {
            return human1;
        }
    }
}