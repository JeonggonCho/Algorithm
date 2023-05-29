function solution(arr, intervals) {
    var answer = [];
    var arr1 = arr.slice(intervals[0][0], intervals[0][1]+1);
    var arr2 = arr.slice(intervals[1][0], intervals[1][1]+1);
    answer = arr1.concat(arr2);
    return answer;
}