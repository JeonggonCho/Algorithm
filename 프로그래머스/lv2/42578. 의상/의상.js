function solution(clothes) {
    var answer = 1;
    var category = {};
    for (let i of clothes) {
        if (category[i[1]] === undefined) {
            category[i[1]] = 1;
        } else {
            category[i[1]]++;
        }
    }
    const quantity = Object.values(category);
    for (let j of quantity) {
        answer *= (j + 1);
    }
    answer--;
    return answer;
}