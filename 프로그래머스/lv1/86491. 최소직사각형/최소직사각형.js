function solution(sizes) {
    var answer = 0;
    // 큰 길이들을 가로 길이로 작은 길이들을 세로 길이로 정렬한 후 가로에서 가장 큰 길이, 세로에서 가장 큰 길이를 구한다.
    for (let i = 0; i < sizes.length; i++) {
        if (sizes[i][0] < sizes[i][1]) {
            var temp = sizes[i][0];
            sizes[i][0] = sizes[i][1];
            sizes[i][1] = temp;
        }
    }
    var widthValue = 0;
    var heightValue = 0;
    for (let j = 0; j < sizes.length; j++) {
        if (sizes[j][0] > widthValue) {
            widthValue = sizes[j][0];
        }
        if (sizes[j][1] > heightValue) {
            heightValue = sizes[j][1];
        }
    }
    answer = widthValue * heightValue;
    return answer;
}