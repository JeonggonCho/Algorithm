function solution(weights) {
    var answer = 0;
    const weight = {};
    const cal = [1, 3/2, 2, 4/3];

    weights.sort((a, b)=> b - a).forEach((x) => {
        let num;
        cal.forEach((i)=>{
            if( num = x * i, weight[num] ){
              answer += weight[num];
            }
        });
        if (!weight[x]) {
            weight[x] = 1;
        } else {
            weight[x]++;
        }
    });
    return answer;
}
