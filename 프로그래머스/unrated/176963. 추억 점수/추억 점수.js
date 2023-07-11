function solution(name, yearning, photo) {
    var answer = [];
    for (let i = 0; i < photo.length; i++) {
        var cnt = 0;
        for (const j of photo[i]) {
            if (name.includes(j)) {
                cnt += yearning[name.indexOf(j)];
            }
        }
        answer.push(cnt);
    }
    return answer;
}