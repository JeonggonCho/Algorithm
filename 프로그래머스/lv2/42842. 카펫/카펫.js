function solution(brown, yellow) {
    const yellowLength = [];
    for (let i = 1; i <= yellow; i++) {
        if (yellow % i === 0) {
            yellowLength.push([i, parseInt(yellow / i)]);
        }
    }
    for (const j of yellowLength) {
        if (j[0] * 2 + j[1] * 2 + 4 === brown && j[0] >= j[1]) {
            return [j[0] + 2, j[1] + 2];
        }
    }
}