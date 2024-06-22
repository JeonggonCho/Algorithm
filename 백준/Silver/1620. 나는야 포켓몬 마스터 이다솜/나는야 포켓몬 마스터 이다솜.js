let fs = require('fs');
let input = fs.readFileSync(0, "utf-8").toString().split('\n');

const [n, m] = input[0].split(' ').map(Number);

const monsters = input.slice(1, n + 1);
const quizzes = input.slice(n + 1, n + m + 1);

let monsterMap = {};

for (let i = 0; i < monsters.length; i++) {
  monsterMap[monsters[i]] = i + 1;
}

let answers = [];

for (let i = 0; i < quizzes.length; i++) {
  if (isNaN(parseInt(quizzes[i]))) {
    answers.push(monsterMap[quizzes[i]].toString());
  } else {
    answers.push(monsters[parseInt(quizzes[i]) - 1]);
  }
}

console.log(answers.join('\n'));