const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    answer = '';
    for (let i = 0; i < str.length; i++) {
        if (str.charAt(i) === str.charAt(i).toLowerCase()) {
            answer += str.charAt(i).toUpperCase();
        } else {
            answer += str.charAt(i).toLowerCase();
        }
    }
    console.log(answer);
});