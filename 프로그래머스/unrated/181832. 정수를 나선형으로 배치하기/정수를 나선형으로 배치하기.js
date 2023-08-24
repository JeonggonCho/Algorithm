function solution(n) {
    const arr = Array.from(Array(n), () => Array(n).fill(0))
    
    let wid = 0;
    let leng = 0;
    let num = 1;
    
    for (let i = n; i > 0; i -= 2) {
        for (let j = 0; j < i; j++) {
            arr[leng][wid++] = num++;
        }
        wid--;
        leng++;
        for (let k = 0; k < i - 1; k++) {
            arr[leng++][wid] = num++;
        }
        leng--;
        wid--;
        for (let l = 0; l < i - 1; l++) {
            arr[leng][wid--] = num++;
        }
        leng--;
        wid++;
        for (let m = 0; m < i - 2; m++) {
            arr[leng--][wid] = num++;
        }
        leng++;
        wid++;
    }
    
    return arr;
}
