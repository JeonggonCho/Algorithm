let fs = require('fs');
const [n, b] = fs.readFileSync('/dev/stdin').toString().split(" ").map(Number);

console.log(n.toString(b).toUpperCase());