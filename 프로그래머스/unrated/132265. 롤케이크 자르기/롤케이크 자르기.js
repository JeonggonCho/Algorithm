// function solution(topping) {
//     var answer = 0;
//     for (let i = 1; i < topping.length; i++) {
//         var obj1 = {};
//         var obj2 = {};
//         var half1 = topping.slice(0, i);
//         var half2 = topping.slice(i);
//         for (const j of half1) {
//             if (obj1[j] === undefined) {
//                 obj1[j] = 1;
//             } else {
//                 obj1[j]++;
//             }
//         }
//         var length1 = Object.keys(obj1).length;
//         for (const k of half2) {
//             if (obj2[k] === undefined) {
//                 obj2[k] = 1;
//             } else {
//                 obj2[k]++;
//             }
//         }
//         var length2 = Object.keys(obj2).length;
//         if (length1 === length2) {
//             answer++;
//         }
//     }
//     return answer;
// }


function solution(topping) {
    var answer = 0;
    var obj1 = {};
    var obj2 = {};
    var length1 = 0;
    var length2 = 0;
    
    for (const i of topping) {
        if (obj2[i] === undefined) {
            obj2[i] = 1;
            length2++;
        } else {
            obj2[i]++;
        }
    }
    
    for (const j of topping) {
        if (obj1[j] === undefined) {
            obj1[j] = 1;
            length1++;
        } else {
            obj1[j]++;
        }
        obj2[j]--;
        if (obj2[j] === 0) {
            delete obj2[j];
            length2--;
        }
        if (length1 === length2) {
            answer++;
        }
    }
    return answer;
}