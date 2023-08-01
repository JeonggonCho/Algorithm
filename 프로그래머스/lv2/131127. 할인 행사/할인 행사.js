function solution(want, number, discount) {
    var answer = 0;
    var wantObj = {};
    for (let i = 0; i < want.length; i++) {
        wantObj[want[i]] = number[i];
    }
    var sortedWant = Object.entries(wantObj).sort();
    for (let j = 0; j <= discount.length - 10; j++) {
        var slicedDiscount = discount.slice(j, j+10);
        var discountObj = {};
        for (const k of slicedDiscount) {
            if (discountObj[k] === undefined) {
                discountObj[k] = 1;
            } else {
                discountObj[k] += 1;
            }
        }
        var sortedDiscount = Object.entries(discountObj).sort();
        if (sortedWant.toString() === sortedDiscount.toString()) {
            answer++;
        }
    }
    return answer;
}