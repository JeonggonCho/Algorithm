function solution(s) {
    let answer = s.length;

    for (let i = 1; i <= parseInt(s.length / 2); i++) {
        let cnt = 0;
        let unit = '';
        let unitCnt = 1;
        
        for (let j = 0; j < s.length; j += i) {
            let slicedStr = s.substring(j, j + i);
            if (unit === slicedStr) {
                unitCnt++;
            } else {
                if (unitCnt > 1) {
                    cnt += unitCnt.toString().length + unit.length;
                } else {
                    cnt += unit.length;
                }
                unit = slicedStr;
                unitCnt = 1;
            }
        }

        if (unitCnt > 1) {
            cnt += unitCnt.toString().length + unit.length;
        } else {
            cnt += unit.length;
        }

        if (cnt < answer) {
            answer = cnt;
        }
    }

    return answer;
}
