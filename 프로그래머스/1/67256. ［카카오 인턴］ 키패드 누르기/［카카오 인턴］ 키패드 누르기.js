function solution(numbers, hand) {
    const pad = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 0, 11]
    ];
    var answer = '';
    let leftHand = 10;
    let rightHand = 11;
    let leftDistance = 0;
    let rightDistance = 0;
    
    for (let i of numbers) {
        if (i === 1) {
            answer += 'L';
            leftHand = 1;
        } else if (i === 4) {
            answer += 'L';
            leftHand = 4;
        } else if (i === 7) {
            answer += 'L';
            leftHand = 7;
        } else if (i === 3) {
            answer += 'R';
            rightHand = 3;
        } else if (i === 6) {
            answer += 'R';
            rightHand = 6;
        } else if (i === 9) {
            answer += 'R';
            rightHand = 9;
        } else if (i === 2) {
            for (let j = 0; j < pad.length; j++) {
                if (pad[j].includes(leftHand)) {
                    leftDistance = Math.abs(j) + Math.abs(pad[j].indexOf(leftHand) - 1);
                }
            }
            for (let k = 0; k < pad.length; k++) {
                if (pad[k].includes(rightHand)) {
                    rightDistance = Math.abs(k) + Math.abs(pad[k].indexOf(rightHand) - 1);
                }
            }
            if (leftDistance === rightDistance) {
                if (hand === 'left') {
                    answer += 'L';
                    leftHand = 2;
                } else {
                    answer += 'R';
                    rightHand = 2;
                }
            } else {
                if (leftDistance > rightDistance) {
                    answer += 'R';
                    rightHand = 2;
                } else {
                    answer += 'L';
                    leftHand = 2;
                }
            }
        } else if (i === 5) {
            for (let l = 0; l < pad.length; l++) {
                if (pad[l].includes(leftHand)) {
                    leftDistance = Math.abs(1 - l) + Math.abs(pad[l].indexOf(leftHand) - 1);
                }
            }
            for (let m = 0; m < pad.length; m++) {
                if (pad[m].includes(rightHand)) {
                    rightDistance = Math.abs(1 - m) + Math.abs(pad[m].indexOf(rightHand) - 1);
                }
            }
            if (leftDistance === rightDistance) {
                if (hand === 'left') {
                    answer += 'L';
                    leftHand = 5;
                } else {
                    answer += 'R';
                    rightHand = 5;
                }
            } else {
                if (leftDistance > rightDistance) {
                    answer += 'R';
                    rightHand = 5;
                } else {
                    answer += 'L';
                    leftHand = 5;
                }
            }
        } else if (i === 8) {
            for (let n = 0; n < pad.length; n++) {
                if (pad[n].includes(leftHand)) {
                    leftDistance = Math.abs(2 - n) + Math.abs(pad[n].indexOf(leftHand) - 1);
                }
            }
            for (let o = 0; o < pad.length; o++) {
                if (pad[o].includes(rightHand)) {
                    rightDistance = Math.abs(2 - o) + Math.abs(pad[o].indexOf(rightHand) - 1);
                }
            }
            if (leftDistance === rightDistance) {
                if (hand === 'left') {
                    answer += 'L';
                    leftHand = 8;
                } else {
                    answer += 'R';
                    rightHand = 8;
                }
            } else {
                if (leftDistance > rightDistance) {
                    answer += 'R';
                    rightHand = 8;
                } else {
                    answer += 'L';
                    leftHand = 8;
                }
            }
        } else if (i === 0) {
            for (let p = 0; p < pad.length; p++) {
                if (pad[p].includes(leftHand)) {
                    leftDistance = Math.abs(3 - p) + Math.abs(pad[p].indexOf(leftHand) - 1);
                }
            }
            for (let q = 0; q < pad.length; q++) {
                if (pad[q].includes(rightHand)) {
                    rightDistance = Math.abs(3 - q) + Math.abs(pad[q].indexOf(rightHand) - 1);
                }
            }
            if (leftDistance === rightDistance) {
                if (hand === 'left') {
                    answer += 'L';
                    leftHand = 0;
                } else {
                    answer += 'R';
                    rightHand = 0;
                }
            } else {
                if (leftDistance > rightDistance) {
                    answer += 'R';
                    rightHand = 0;
                } else {
                    answer += 'L';
                    leftHand = 0;
                }
            }
        }
    }
    return answer;
}