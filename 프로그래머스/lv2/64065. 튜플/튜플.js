function solution(s) {
    let arr1 = [];
    let answer = [];
    let arr2 = s.substr(2, s.length-4).split("},{");
    for (const i of arr2) {
        var a = i.split(",").map(x => parseInt(x));
        arr1.push(a);
    }
    let arr3 = [];
    for (let j = 1; j <= arr1.length; j++) {
        for (const k of arr1) {
            if (j === k.length) {
                arr3.push(k);
            }
        }
    }
    answer.push(...arr3[0]);
    for (let l = 0; l < arr3.length - 1; l++) {
        let difference = arr3[l + 1].filter(x => !arr3[l].includes(x));
        answer.push(...difference);
    }
    return answer;
}