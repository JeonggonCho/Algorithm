let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = parseInt(input[0]);
const powers = input[1].split(' ').map(Number);

powers.reverse();

let LIS = [powers[0]];

const binarySearch = (arr, val) => {
  let left = 0;
  let right = arr.length - 1;
  while (left < right) {
    let mid = Math.floor((left + right) / 2);
    if (arr[mid] < val) left = mid + 1;
    else right = mid;
  }
  return left;
};

for (let i = 1; i < powers.length; i++) {
  if (powers[i] > LIS[LIS.length - 1]) {
    LIS.push(powers[i]);
  } else {
    let pos = binarySearch(LIS, powers[i]);
    LIS[pos] = powers[i];
  }
}

console.log(n - LIS.length);
