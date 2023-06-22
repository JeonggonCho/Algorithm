function solution(arr, queries) {
    for (const i of queries) {
        var temp = arr[i[0]];
        arr[i[0]] = arr[i[1]];
        arr[i[1]] = temp;
    }
    return arr;
}