let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [n, m] = input[0].split(" ").map(Number);
const cases = input.slice(1, m + 1).map(x => x.split(" ").map(Number));

let basket = new Array(n).fill(0).map((_, index) => index + 1);

for (let i = 0; i < cases.length; i++) {
  let slicedBasket = basket.slice(cases[i][0] - 1, cases[i][1]);
  let reversedBasket = slicedBasket.reverse();
  basket = basket.slice(0, cases[i][0] - 1).concat(reversedBasket, basket.slice(cases[i][1], basket.length));
}

console.log(basket.join(" "));