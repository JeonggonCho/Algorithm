let fs = require('fs');
let input = Number(fs.readFileSync('/dev/stdin'));

const factorial = n => {
  if (n === 1) return 1;
  return n * factorial(n - 1);
};

if (input === 0) {
  return console.log(1);
} else {
  return console.log(factorial(input));
}