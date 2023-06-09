function solution(number) {
    var answer = 0;
    var sumNum = 0;
    for (i = 0; i < number.length; i++) {
        sumNum += parseInt(number.charAt(i));
    }
    answer = sumNum % 9;
    return answer;
}