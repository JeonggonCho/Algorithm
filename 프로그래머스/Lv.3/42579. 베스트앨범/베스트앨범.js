function solution(genres, plays) {
    var answer = [];
    const genresPlaysCnt = {};
    const genresSorting = {};
    
    for (let i = 0; i < genres.length; i++) {
        let genre = genres[i];
        if (genresPlaysCnt[genre] === undefined) {
            genresPlaysCnt[genre] = plays[i];
        } else {
            genresPlaysCnt[genre] += plays[i];
        }
        if (genresSorting[genre] === undefined) {
            genresSorting[genre] = [i];
        } else {
            genresSorting[genre].push(i);
        }
    }
    
    for (const genre of Object.keys(genresSorting)) {
        genresSorting[genre].sort((a, b) => {
            if (plays[a] > plays[b]) {
                return -1;
            } else {
                return 1;
            }
        })
        answer = answer.concat(genresSorting[genre].slice(0, 2));
    }
    
    
    answer.sort((a, b) => {
        if (genresPlaysCnt[genres[a]] > genresPlaysCnt[genres[b]]) {
            return -1;
        } else if (genresPlaysCnt[genres[a]] < genresPlaysCnt[genres[b]]) {
            return 1;
        } else if (plays[a] > plays[b]) {
            return -1;
        } else if (plays[a] < plays[b]) {
            return 1;
        } else if (a > b) {
            return 1;
        } else {
            return -1;
        }
    })
    return answer;
}