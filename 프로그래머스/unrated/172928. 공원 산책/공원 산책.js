function solution(park, routes) {
    const vertical = park.length;
    const horizon = park[0].length;
    var blocks = [];
    
    for (let i = 0; i < vertical; i++) {
        for (let j = 0; j < horizon; j++) {
            if (park[i][j] === "S") {
                var position = [i, j];
            } else if (park[i][j] === "X") {
                blocks.push([i, j]);
            }
        }
    }
    
    for (const k of routes) {
        var route = k.split(" ");
        var direction = route[0];
        var dist = Number(route[1]);
        
        if (direction === "E") {
            var arrival = position[1] + dist;
            if (arrival < horizon) {
                var check = true;
                var origin = position[1];
                for (let l = 0; l < dist; l++) {
                    position[1]++;
                    if (blocks.some(x => x[0] === position[0] && x[1] === position[1])) {
                        check = false;
                        position[1] = origin;
                        break;
                    }
                }
                if (check === true) {
                    position[1] = arrival;
                }
            }
            
        } else if (direction === "W") {
            var arrival = position[1] - dist;
            if (arrival >= 0) {
                var check = true;
                var origin = position[1];
                for (let m = 0; m < dist; m++) {
                    position[1]--;
                    if (blocks.some(x => x[0] === position[0] && x[1] === position[1])) {
                        check = false;
                        position[1] = origin;
                        break;
                    }
                }
                if (check === true) {
                    position[1] = arrival;
                }
            }
            
        } else if (direction === "S") {
            var arrival = position[0] + dist;
            if (arrival < vertical) {
                var check = true;
                var origin = position[0];
                for (let n = 0; n < dist; n++) {
                    position[0]++;
                    if (blocks.some(x => x[0] === position[0] && x[1] === position[1])) {
                        check = false;
                        position[0] = origin;
                        break;
                    }
                }
                if (check === true) {
                    position[0] = arrival;
                }
            }
            
        } else if (direction === "N") {
            var arrival = position[0] - dist;
            if (arrival >= 0) {
                var check = true;
                var origin = position[0];
                for (let o = 0; o < dist; o++) {
                    position[0]--;
                    if (blocks.some(x => x[0] === position[0] && x[1] === position[1])) {
                        check = false;
                        position[0] = origin;
                        break;
                    }
                }
                if (check === true) {
                    position[0] = arrival;
                }
            }
        }
    }
    return position;
}