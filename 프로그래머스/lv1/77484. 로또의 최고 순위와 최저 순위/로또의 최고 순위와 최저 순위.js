function solution(lottos, win_nums) {
    var rank = [6, 5, 4, 3, 2]; // 맞는 번호 개수의 (인덱스+1)이 순위
    var win = 0; // 맞는 번호 개수
    var zero = 0; // 0의 개수
    
    for (const i of lottos) {
        if (i !== 0 && win_nums.includes(i)) {
            win++;
        } else if (i === 0) {
            zero++;
        }
    }
    
    var high = win + zero;
    if (high >= 2) {
        var highRank = rank.indexOf(high) + 1;
    } else {
        var highRank = 6
    }
    
    if (win >= 2) {
        var lowRank = rank.indexOf(win) + 1;
    } else {
        var lowRank = 6;
    }
    
    return [highRank, lowRank];
}