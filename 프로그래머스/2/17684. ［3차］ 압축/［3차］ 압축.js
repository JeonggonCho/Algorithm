let chars = {};
for (let i = 65; i <= 90; i++) {
    chars[String.fromCharCode(i)] = i - 64;
}

function findLongestPrefix(chars, msg) {
    let current = '';
    let longest = '';

    for (let char of msg) {
        current += char;
        if (chars[current] === undefined) {
            break;
        }
        longest = current;
    }

    return longest;
}

function solution(msg) {
    let answer = [];
    let idx = 27;

    while (msg.length > 0) {
        let result = findLongestPrefix(chars, msg);
        answer.push(chars[result]);

        let current = result + msg.charAt(result.length);
        chars[current] = idx;
        idx++;

        msg = msg.slice(result.length);
    }

    return answer;
}
