let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const cities = Number(input[0]);
const dists = input[1].split(" ").map(Number);
const prices = input[2].split(" ").map(Number);

let minPrice = prices[0];
for (let i = 0; i < cities; i++) {
  minPrice = Math.min(minPrice, prices[i]);
  prices[i] = minPrice;
}

let answer = BigInt(0);
for (let j = 0; j < cities - 1; j++) {
  answer += BigInt(dists[j]) * BigInt(prices[j]);
}

console.log(String(answer));