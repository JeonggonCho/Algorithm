function solution(ingredient) {
    var answer = 0;
    var burger = [1, 2, 3, 1];
    var stack = [];
    
    for (let i = 0; i < ingredient.length; i++) {
        var topping = ingredient[i];
        stack.push(topping);
        
        if (stack.length >= burger.length) {
            var lastItems = stack.slice(-burger.length);
            
            if (isEqual(lastItems, burger)) {
                answer++;
                stack.splice(-burger.length);
            }
        }
    }
    
    return answer;
}

function isEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) {
        return false;
    }
    
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) {
            return false;
        }
    }
    
    return true;
}
