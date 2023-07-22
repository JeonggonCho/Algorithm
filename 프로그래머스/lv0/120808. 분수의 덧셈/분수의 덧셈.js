function solution(numer1, denom1, numer2, denom2) {
    var numer = numer1 * denom2 + numer2 * denom1;
    var denom = denom1 * denom2;
    let num = (numer > denom) ? numer : denom;
    for (let i = num; i > 0; i--) {
        if (numer % i === 0 && denom % i === 0) {
            numer = numer / i;
            denom = denom / i;
        }
    }
    return [numer, denom];
}