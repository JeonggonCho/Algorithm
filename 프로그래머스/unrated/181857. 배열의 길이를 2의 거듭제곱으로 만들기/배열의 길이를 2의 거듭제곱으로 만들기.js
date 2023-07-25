function solution(arr) {
    var len = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024];
    while (!len.includes(arr.length)) {
        arr.push(0);
    }
    return arr;
}