function solution(k, tangerine) {
    var answer = 0;
    var arr = {};
    for (const i of tangerine) {
        if (arr[i] === undefined) {
            arr[i] = 1;
        } else {
            arr[i]++;
        }
    }
    let sorted = Object.entries(arr).sort((a, b) => b[1] - a[1]);
    for (const j of sorted) {
        if (k > j[1]) {
            answer++;
            k -= j[1];
        } else if (k <= j[1]) {
            answer++;
            break;
        }
    }
    return answer;
}