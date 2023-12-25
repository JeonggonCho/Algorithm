function solution(order) {
    let answer = 0;
    const container = [];
    for (let i = 1; i <= order.length; i++) {
        container.push(i);
    }
    const stack = [];
    let orderIdx = 0;
    let containerIdx = 0;

    while (answer < order.length) {
        const orderBox = order[orderIdx];
        
        if (orderBox === container[containerIdx]) {
            containerIdx++;
            orderIdx++;
            answer++;
        } else if (orderBox === stack[stack.length-1]) {
            stack.pop();
            orderIdx++;
            answer++;
        } else if (container[containerIdx] > orderBox) {
            break;
        } else {
            stack.push(container[containerIdx]);
            containerIdx++;
        }
    }

    return answer;
}