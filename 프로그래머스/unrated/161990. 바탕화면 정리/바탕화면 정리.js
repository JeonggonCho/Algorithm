function solution(wallpaper) {
    var x = [];
    var y = [];
    for (let i = 0; i < wallpaper.length; i++) {
        for (let j = 0; j < wallpaper[i].length; j++) {
            if (wallpaper[i][j] === '#') {
                y.push(i);
                x.push(j);
            }
        }
    }
    x.sort(function(a, b) {
        return a - b;
    });
    y.sort(function(a, b) {
        return a - b;
    });
    const answer = [y[0], x[0], y.at(-1) + 1, x.at(-1) + 1];
    return answer;
}