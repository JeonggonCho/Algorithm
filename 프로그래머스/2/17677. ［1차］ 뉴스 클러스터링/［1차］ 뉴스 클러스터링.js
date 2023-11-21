function slicedArr(str) {
    let arr = [];
    for (let i = 0; i < str.length - 1; i++) {
        let sliced = str.slice(i, i+2);
        if (sliced[0].charCodeAt() >= 65 && sliced[0].charCodeAt() <= 90
            && sliced[1].charCodeAt() >= 65 && sliced[1].charCodeAt() <= 90) {
            arr.push(sliced);
        }
    }
    return arr;
}

function intersection(arr1, arr2) {
  const result = [];
  const countMap = {};

  for (const value of arr1) {
    if (countMap[value] === undefined) {
      countMap[value] = 1;
    } else {
      countMap[value]++;
    }
  }

  for (const value of arr2) {
    if (countMap[value] !== undefined && countMap[value] > 0) {
      result.push(value);
      countMap[value]--;
    }
  }
  return result;
}

function union(arr1, arr2) {
  const arr = [...arr1, ...arr2];
  return arr;
}

function solution(str1, str2) {
    let upperStr1 = str1.toUpperCase();
    let upperStr2 = str2.toUpperCase();
    
    let arr1 = slicedArr(upperStr1);
    let arr2 = slicedArr(upperStr2);
    
    if (arr1.length == 0 && arr2.length == 0) {
        return 65536;
    } else {
        const intersectCnt = intersection(arr1, arr2).length;
        const unionCnt = union(arr1, arr2).length - intersectCnt;
        const result = Math.floor((intersectCnt / unionCnt) * 65536);
        
        return result;
    }
}