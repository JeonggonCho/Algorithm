let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(" ");

const n = input[0];
const b = Number(input[1]);

let answer = parseInt(n, b);

console.log(answer);