function solution(myString, pat) {
    var reversedString = myString.split("").reverse().join("");
    var reversedPat = pat.split("").reverse().join("");
    const num = reversedString.indexOf(reversedPat);
    const answer = myString.slice(0, myString.length - num);
    return answer;
}