function findElement(board, num) {
    for (let i = 0; i < board.length; i++) {
        if (board[i][num] !== 0) {
            const returnValue = board[i][num];
            board[i][num] = 0;
            return returnValue;
        }
    }
    return null;
}

function solution(board, moves) {
    const stack = new Array();
    let answer = 0;
    for (let j of moves) {
        const item = findElement(board, j - 1);
        if (item !== null) {
            if (stack.length === 0) {
                stack.push(item);
            } else if (stack[stack.length - 1] === item) {
                answer++;
                stack.pop();
            } else {
                stack.push(item);
            }
        }
    }
    return answer * 2;
}