function solution(my_string, queries) {
    for (const i of queries) {
        var my_stringArr = my_string.split('');
        var reversed = my_stringArr.slice(i[0], i[1]+1).reverse().join('');
        my_stringArr.splice(i[0], i[1] - i[0] +1, reversed);
        my_string = my_stringArr.join('');
    }
    return my_string;
}