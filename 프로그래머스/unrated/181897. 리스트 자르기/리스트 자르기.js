function solution(n, slicer, num_list) {
    var answer = [];
    if (n === 1) {
        answer = num_list.slice(0, slicer[1]+1);
    } else if (n === 2) {
        answer = num_list.slice(slicer[0]);
    } else if (n === 3) {
        answer = num_list.slice(slicer[0], slicer[1]+1);
    } else if (n === 4) {
        var arr = [];
        arr = num_list.slice(slicer[0], slicer[1]+1);
        for (i = 0; i < arr.length; i++) {
            if (i % slicer[2] === 0) {
                answer.push(arr[i]);
            }
        }
    }
    return answer;
}