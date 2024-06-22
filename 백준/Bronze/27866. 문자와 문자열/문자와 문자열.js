let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let character = input[0];
let i = Number(input[1]);

console.log(character[i - 1]);