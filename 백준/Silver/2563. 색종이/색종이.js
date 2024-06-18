let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const papers = Number(input[0]);
const coordinate = input.slice(1, papers + 1).map(x => x.split(" ").map(Number));

function getPoints([a, b]) {
  let points = [];
  for (let k = 0; k < 10; k++) {
    for (let l = 0; l < 10; l++) {
      points.push([a+k, b+l]);
    }
  }
  return points;
}

let totalPoints = new Set();

for (let i of coordinate) {
  let points = getPoints(i);
  for (let j of points) {
    totalPoints.add(j.toString());
  }
}

console.log(totalPoints.size);