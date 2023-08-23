function solution(dirs) {
    var answer = 0;
    var position = [0, 0];
    var history = [];
    for (const i of dirs) {
        if (i === "U") {
            var move = [position[0], position[1] + 1];
            if (boundary(move)) {
                var route = [(position[0] + move[0]) / 2, (position[1] + move[1]) / 2];
                if (!history.some((x) => route[0] === x[0] && route[1] === x[1])) {
                    history.push(route);
                    answer++;
                }
                position = move;
            }
        } else if (i === "D") {
            var move = [position[0], position[1] - 1];
            if (boundary(move)) {
                var route = [(position[0] + move[0]) / 2, (position[1] + move[1]) / 2];
                if (!history.some((x) => route[0] === x[0] && route[1] === x[1])) {
                    history.push(route);
                    answer++;
                }
                position = move;
            }
        } else if (i === "R") {
            var move = [position[0] + 1, position[1]];
            if (boundary(move)) {
                var route = [(position[0] + move[0]) / 2, (position[1] + move[1]) / 2];
                if (!history.some((x) => route[0] === x[0] && route[1] === x[1])) {
                    history.push(route);
                    answer++;
                }
                position = move;
            }
        } else if (i === "L") {
            var move = [position[0] - 1, position[1]];
            if (boundary(move)) {
                var route = [(position[0] + move[0]) / 2, (position[1] + move[1]) / 2];
                if (!history.some((x) => route[0] === x[0] && route[1] === x[1])) {
                    history.push(route);
                    answer++;
                }
                position = move;
            }
        }
    }
    return answer;
}

function boundary(arr) {
    if (arr[0] >= -5 && arr[0] <= 5 && arr[1] >= -5 && arr[1] <= 5) {
        return true;
    } else {
        return false;
    }
}