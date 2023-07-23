function solution(answers) {
    const answer = [];
    var arr = {};
    var arr1 = [];
    var arr2 = [];
    var arr3 = [];
    // 1번 수포자
    for (let i = 0; i < answers.length; i++) {
        arr1.push(i % 5 + 1);
    }
    // 2번 수포자
    var sampleArr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    for (let j = 0; j < answers.length; j++) {
        arr2.push(sampleArr2[j % 8]);
    }
    // 3번 수포자
    var sampleArr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for (let k = 0; k < answers.length; k++) {
        arr3.push(sampleArr3[k % 10]);
    }
    
    // 문제 검사
    for (let l = 0; l < answers.length; l++) {
        var num = answers[l];
        if (arr1[l] === num) {
            if (1 in arr) {
                arr[1] += 1;
            } else {
                arr[1] = 0;
            }
        }
        if (arr2[l] === num) {
            if (2 in arr) {
                arr[2] += 1;
            } else {
                arr[2] = 0;
            }
        }
        if (arr3[l] === num) {
            if (3 in arr) {
                arr[3] += 1;
            } else {
                arr[3] = 0;
            }
        }
    }
    var maxScore = Math.max(...Object.values(arr));
    for (const m in arr) {
        if (arr[m] === maxScore) {
            answer.push(parseInt(m));
        }
    }
    return answer;
}