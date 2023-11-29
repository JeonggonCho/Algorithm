function getPermutations(arr) {
  const result = [];

  function generatePermutations(currentArr, remainingArr) {
    if (remainingArr.length === 0) {
      result.push(currentArr.slice());
      return;
    }

    for (let i = 0; i < remainingArr.length; i++) {
      const nextArr = currentArr.concat(remainingArr[i]);
      const nextRemainingArr = remainingArr.slice(0, i).concat(remainingArr.slice(i + 1));
      generatePermutations(nextArr, nextRemainingArr);
    }
  }

  generatePermutations([], arr);
  return result;
}

function solution(k, dungeons) {
    const permutations = getPermutations(dungeons);
    let answer = 0;
    
    for (let j of permutations) {
        let cnt = 0;
        let health = k;
        
        for (let l = 0; l < j.length; l += 2) {
            let neededHealth = j[l];
            let usedHealth = j[l + 1];
            if (health >= neededHealth) {
                health -= usedHealth;
                cnt += 1;
            }
            if (answer < cnt) {
                answer = cnt;
            }
        }
    }
    return answer;
}