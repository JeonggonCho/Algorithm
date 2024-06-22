let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(" ").map(Number);
const cases = input.slice(1, m + 1).map(x => x.split(" ").map(Number));

let basket = new Array(n).fill(0);

for (let i = 0; i < cases.length; i++) {
  for (let j = cases[i][0]; j <= cases[i][1]; j++) {
    basket[j - 1] = cases[i][2];
  }
}

console.log(basket.join(" "));