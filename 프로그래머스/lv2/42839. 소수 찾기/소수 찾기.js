function solution(numbers) {
    var answer = 0;
    const numArr = numbers.split("");
    numArr.sort(function(a, b)  {
        return b - a;
    });
    const maxNum = Number(numArr.join(""));
    var divArr = [];
    for (let i = 2; i <= maxNum; i++) {
        var check = true;
        for (let j = 2; j * j <= i; j++) { // 제곱근 이하의 수로 나누기
            if (i % j === 0) {
                check = false;
                break;
            }
        }
        if (check === true) {
            var iArr = i.toString().split("");
            let difference = [...numArr];
            for (let k of iArr) {
                if (difference.includes(k)) {
                    difference.splice(difference.indexOf(k), 1);
                } else {
                    check = false;
                    break;
                }
            }
            if (check === true) {
                divArr.push(i);
            }
        }
    }
    return divArr.length;
}
