function solution(progresses, speeds) {
    var answer = [];
    var arr = [];
    for (let i = 0; i < progresses.length; i++) {
        var leftDays = Math.ceil((100 - progresses[i]) / speeds[i])
        arr.push(leftDays);
    }
    var works = 1;
    var longtermWork = arr[0];
    for (let j = 1; j <= arr.length; j++) {
        if (arr[j] <= longtermWork) {
            works++;
        } else {
            answer.push(works);
            works = 1;
            longtermWork = arr[j];
        }
    }
    return answer;
}