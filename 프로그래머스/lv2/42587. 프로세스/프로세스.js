function solution(priorities, location) {
    var obj = {};
    let activateArr = [];
    let cnt = priorities.length;
    for (let i = 0; i < cnt; i++) {
        obj[i] = priorities[i];
    }
    let objArr = Object.entries(obj);
    while (activateArr.length !== cnt) {
        var firstObjValue = objArr.shift();
        if (firstObjValue[1] < Math.max(...value(objArr))) {
            objArr.push(firstObjValue);
        } else {
            activateArr.push(firstObjValue);
        }
    }
    for (const k of activateArr) {
        if (Number(k[0]) === location) {
            var answer = activateArr.indexOf(k) + 1;
        }
    }
    return answer;
}

function value(arr) {
    var valueArr = [];
    for (const j of arr) {
        valueArr.push(j[1]);
    }
    return valueArr;
}