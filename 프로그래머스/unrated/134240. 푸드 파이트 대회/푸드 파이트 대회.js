function solution(food) {
    var arr = '';
    for (let i = 0; i < food.length; i++) {
        if (i > 0) {
            if (food[i] % 2 === 0) {
                arr += i.toString().repeat(food[i] / 2);
            } else {
                arr += i.toString().repeat((food[i]-1) / 2);
            }
        }
    }
    const reversedArr = arr.split('').reverse().join('');
    var answer = arr + '0' + reversedArr;
    return answer;
}