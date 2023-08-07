function solution(id_list, report, k) {
    var reportSet = [...new Set(report)];
    var obj = {};
    var resultObj = {};
    for (const i of id_list) {
        obj[i] = 0;
        resultObj[i] = 0;
    }
    var newIdList = [];
    for (const j of reportSet) {
        var splitId = j.split(" ")
        newIdList.push(splitId);
        obj[splitId[1]]++;
    }
    for (const l of id_list) {
        for (const m of newIdList) {
            if (m[0] === l && obj[m[1]] >= k) {
                resultObj[l]++;
            }
        }
    }
    return Object.values(resultObj);
}