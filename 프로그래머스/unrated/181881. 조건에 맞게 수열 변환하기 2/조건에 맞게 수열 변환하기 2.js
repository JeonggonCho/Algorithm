function solution(arr) {
  var answer = 0;
  while (true) {
    var compareArr = [];
    for (let i = 0; i < arr.length; i++) {
      if (arr[i] >= 50 && arr[i] % 2 === 0) {
        compareArr.push(arr[i] / 2);
      } else if (arr[i] < 50 && arr[i] % 2 !== 0) {
        compareArr.push(arr[i] * 2 + 1);
      } else {
        compareArr.push(arr[i]);
      }
    }
    
    // 내용물 비교
    const isSame = arr.length === compareArr.length && arr.every((value, index) => value === compareArr[index]);
    if (isSame) {
      return answer;
    } else {
      answer += 1;
      arr = compareArr;
    }
  }
}
