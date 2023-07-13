function solution(a, b) {
    var week = new Array('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT');
    var day = new Date(`2016-${a}-${b}`).getDay();
    var answer = week[day];
    return answer;
}