let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split("\n");

const [n, m] = input[0].split(" ").map(Number);
const cases = input.slice(1, m + 1).map(x => x.split(" ").map(Number));

let basket = new Array(n).fill(0).map((_, index) => index + 1);

for (let i = 0; i < cases.length; i++) {
  let tmp = basket[cases[i][0] - 1];
  basket[cases[i][0] - 1] = basket[cases[i][1] - 1];
  basket[cases[i][1] - 1] = tmp;
}

console.log(basket.join(" "));