function solution(str1, str2) {
    var answer = '';
    for (i = 0; i < str1.length; i++) {
        answer += str1.charAt(i);
        answer += str2.charAt(i);
    }
    return answer;
}

// '문자열'.charAt('인덱스') = 문자열 꺼내기