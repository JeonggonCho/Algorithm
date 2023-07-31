function solution(elements) {
    var answer = 0;
    let arr = [];
    for (let i = 0; i < elements.length; i++) {
        for (let j = 1; j <= elements.length; j++) {
            if (i + j <= elements.length) {
                var slicedArr = elements.slice(i, i + j);
            } else {
                var slicedArr = elements.slice(i, elements.length).concat(elements.slice(0, i + j - elements.length));
            }
            const result = slicedArr.reduce(function add(sum, currValue) {
                return sum + currValue;
            }, 0);
            arr.push(result);
        }
    }
    const set = new Set(arr);
    const setArr = [...set];
    return setArr.length;
}