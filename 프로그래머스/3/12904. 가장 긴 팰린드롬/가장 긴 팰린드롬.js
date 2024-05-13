function isPalindrome(s, start, end) {
    while (start < end) {
        if (s[start] !== s[end]) return false;
        start++;
        end--;
    }
    return true;
}

function solution(s) {
    if (s.length <= 1) return s.length;

    let maxLength = 1;

    for (let start = 0; start < s.length; start++) {
        for (let end = s.length - 1; end > start; end--) {
            if (end - start + 1 <= maxLength) break;
            if (isPalindrome(s, start, end)) {
                maxLength = end - start + 1;
                break;
            }
        }
    }

    return maxLength;
}
