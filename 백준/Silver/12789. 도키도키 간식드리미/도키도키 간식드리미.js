let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const n = Number(input[0]);
let arr = input[1].split(' ').map(x => Number(x));
let reversedArr = arr.reverse();

let stack = [];
let cur = 1;

while (reversedArr.length > 0) {
  let number = reversedArr.pop();

  if (number === cur) {
    cur++;
  } else if (stack.length > 0 && stack[stack.length - 1] === cur) {
    stack.pop();
    cur++;
    reversedArr.push(number);
  } else {
    stack.push(number);
  }
}

while (stack.length > 0 && stack[stack.length - 1] === cur) {
  stack.pop();
  cur++;
}

if (stack.length === 0) {
  console.log("Nice");
} else {
  console.log("Sad");
}