function solution(n, words) {
    var arr = [];
    for (let i = 0; i < words.length; i++) {
        // 이미 앞에서 나온 단어일 경우
        if (arr.includes(words[i])) {
            return [i % n + 1, Math.floor(i / n) + 1];
        } else {
            arr.push(words[i]);
        }
        
        // 앞단어의 마지막 글자로 시작하지 않을 경우
        if (i > 0) {
            if (words[i].charAt(0) !== words[i-1].charAt(words[i-1].length - 1)) {
                return [i % n + 1, Math.floor(i / n) + 1];
            }
        }
        
        // 한글자 단어인 경우
        if (words[i].length === 1) {
            return [i % n + 1, Math.floor(i / n) + 1];
        }
    }
    // 탈락자가 없을 경우
    return [0, 0];
}