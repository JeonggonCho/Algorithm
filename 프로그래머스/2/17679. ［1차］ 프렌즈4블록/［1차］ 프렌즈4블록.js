function solution(m, n, board) {
    let newBoard = board.map(x => x.split(""));
    let answer = 0;
    let blocks;
    
    do {
        blocks = new Array();
        for (let i = 0; i < (m - 1); i++) {
            for (let j = 0; j < (n - 1); j++) {
                if (newBoard[i][j] === undefined) {
                    continue;
                } else if (newBoard[i][j] === newBoard[i+1][j] && newBoard[i][j] === newBoard[i][j+1] && newBoard[i][j] === newBoard[i+1][j+1]) {
                    const indexes = [[i, j], [i, j+1], [i+1, j], [i+1, j+1]];
                    for (let k of indexes) {
                        blocks.push(k);
                    }
                }
            }
        }
        
        for (let l of blocks) {
            if (newBoard[l[0]][l[1]] !== undefined) {
                newBoard[l[0]][l[1]] = undefined;
                answer++;
            }
        }
        
        newBoard = moveByGravity(m, n, newBoard);
    } while (blocks.length !== 0);
    
    return answer;
}

function moveByGravity(m, n, arr) {
    let movedBoard = new Array();
    for (let o = 0; o < m; o++) {
        movedBoard.push([]);
    }
    for (let p = 0; p < n; p++) {
        let emptyArr = new Array();
        let existArr = new Array();
        for (let q = 0; q < m; q++) {
            if (arr[q][p] === undefined) {
                emptyArr.push(undefined);
            } else {
                existArr.push(arr[q][p]);
            }
        }
        let combinationArr = emptyArr.concat(existArr);
        for (let r = m-1; r >= 0; r--) {
            movedBoard[r].push(combinationArr[r]);
        }
    }
    return movedBoard;
}
