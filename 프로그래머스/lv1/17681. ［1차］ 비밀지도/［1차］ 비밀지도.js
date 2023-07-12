function solution(n, arr1, arr2) {
    var charArr1 = [];
    var charArr2 = [];
    var answer = [];
    for (const i of arr1) {
        var binary = i.toString(2);
        var converted1 = '0'.repeat(n - binary.length) + binary;
        charArr1.push(converted1);
    }
    for (const j of arr2) {
        var binary = j.toString(2);
        var converted2 = '0'.repeat(n - binary.length) + binary;
        charArr2.push(converted2);
    }
    for (let k = 0; k < n; k++) {
        var temp = '';
        for (let l = 0; l < n; l++) {
            if (charArr1[k].charAt(l) === '0' && charArr2[k].charAt(l) === '0') {
                temp += ' ';
            } else {
                temp += '#';
            }
        }
        answer.push(temp);
    }
    return answer;
}