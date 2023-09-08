function solution(keymap, targets) {
    var answer = [];
    var keyIndex = {};
    
    for (const i of keymap) {
        for (const j of i) {
            if (keyIndex[j] === undefined) {
                keyIndex[j] = i.indexOf(j) + 1;
            } else if (keyIndex[j] > i.indexOf(j) + 1) {
                keyIndex[j] = i.indexOf(j) + 1;
            }
        }
    }
    
    for (const k of targets) {
        var cnt = 0;
        var check = true;
        var key = Object.keys(keyIndex);
        for (const l of k) {
            if (key.includes(l)) {
                cnt += keyIndex[l];
            } else {
                answer.push(-1);
                check = false;
                break;
            }
        }
        if (check === true) {
            answer.push(cnt);
        }
    }
    return answer;
}