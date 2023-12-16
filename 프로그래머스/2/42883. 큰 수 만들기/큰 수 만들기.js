function solution(number, k) {
    let arr = [];
    let numbers = number.split("").map(Number).reverse();
    
    while (numbers.length > 0 && k !== 0) {
        let num = numbers.pop();
        
        if (arr.length === 0 || arr[arr.length - 1] >= num) {
            arr.push(num);
        } else {
            while(arr.length > 0 && arr[arr.length - 1] < num && k > 0) {
                arr.pop();
                k -= 1;
            }
            arr.push(num);
        }
    }
    
    while (k !== 0) {
        arr.pop();
        k -= 1;
    }
    
    if (numbers.length > 0) {
        arr = arr.concat(numbers.reverse());
    }
    
    let answer = arr.map(String).join('');
    return answer;
}