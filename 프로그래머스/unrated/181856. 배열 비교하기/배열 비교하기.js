function solution(arr1, arr2) {
    var answer = 0;
    var i = length(arr1, arr2);
    if (i !== 0) {
        answer = i;
    } else {
        if (add(arr1) > add(arr2)) {
            answer = 1;
        } else if (add(arr1) < add(arr2)) {
            answer = -1;
        } else {
            answer = 0;
        }
    } return answer;
    
}

length = function(a, b) {
    var answer = 0;
    if (a.length > b.length) {
        answer = 1;
    } else if (a.length < b.length) {
        answer = -1;
    } else {
        answer = 0;
    }
    return answer;
}

add = function(arr) {
    return arr.reduce((a, b) => a + b, 0);
};