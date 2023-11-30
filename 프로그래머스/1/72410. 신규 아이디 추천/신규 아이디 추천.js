// 아이디의 문자로 가능한 아스키번호 배열 ascii: 빼기 45, 마침표 46, 밑줄 95
let ascii = [45, 46, 95];
    
// ascii배열에 알파벳 소문자의 아스키번호 넣기
for (let i = 97; i <= 122; i++) {
    ascii.push(i);
}
    
// ascii배열에 숫자의 아스키번호 넣기
for (let j = 48; j <= 57; j++) {
    ascii.push(j);
}

// 아이디 규칙 함수
function isId(id) {
    
    // 아이디의 모든 문자를 아스키번호로 변환한 배열 idAscii
    let idAscii = [];
    for (let k of id) {
        idAscii.push(k.charCodeAt());
    }
    
    // 모든 idAscii의 요소가 ascii에 포함되는지 판단
    const isInclude = idAscii.every(item => ascii.includes(item));
    
    if (id.length < 3 || id.length > 15) { // 아이디 길이가 3미만 15초과이면 false리턴
        return false;
    } else if (!isInclude) { // 아이디의 아스키번호가 아이디로 가능한 아스키번호에 없다면 false리턴
        return false;
    } else if (id.startsWith('.') || id.endsWith('.') || id.includes('..')) { // 마침표로 시작하거나, 끝나거나, 연속사용된 경우 false리턴
        return false;
    }
    // 모든 규칙을 충족시 true리턴
    return true;
}

// 1단계 : 모든 대문자를 소문자로 치환
function stage1(id) {
    return id.toLowerCase();
}

// 2단계 : 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
function stage2(id) {
    let newId = '';
    for (let l of id) {
        if (ascii.includes(l.charCodeAt())) {
            newId += l;
        }
    }
    return newId;
}

// 3단계 : 마침표가 연속2번 이상된 부분을 하나의 마침표로 치환
function stage3(id) {
    let newId = '';
    for (let m of id) {
        if (newId.length === 0) {
            newId += m;
        } else if (newId.charAt(newId.length - 1) === '.' && m !== '.') {
            newId += m;
        } else if (newId.charAt(newId.length - 1) !== '.') {
            newId += m;
        }
    }
    return newId;
}

// 4단계 : 마침표가 처음이나 끝에 위치한다면 제거
function stage4(id) {
    if (id.startsWith('.')) {
        id = id.slice(1);
    }
    if (id.endsWith('.')) {
        id = id.slice(0, -1);
    }
    return id;
}

// 5단계 : 빈 문자열이라면 'a'리턴
function stage5(id) {
    if (id.length === 0) {
        return 'a';
    }
    return id;
}

// 6단계 : id의 길이가 16자 이상이면, 첫 15개 이외의 문자들 제거, 만약 제거 후, 끝이 마침표이면, 끝의 마침표도 제거
function stage6(id) {
    if (id.length >= 16) {
        id = id.substring(0, 15);
    }
    if (id.endsWith('.')) {
        id = id.slice(0, -1);
    }
    return id;
}

// 7단계 : id의 길이가 2자 이하라면, id의 마지막 문자를 id의 길이가 3이 될 때까지 반복해서 끝에 붙이기
function stage7(id) {
    while (id.length <= 2) {
        id += id.charAt(id.length - 1);
    }
    return id;
}

function solution(new_id) {
    var answer = '';
    if (isId(new_id)) { // 아이디 규칙 함수를 통해 true가 반환되면 new_id 그대로 리턴
        return new_id;
    } else { // 그렇지 않을 경우, 새로운 아이디 생성하여 추천
        new_id = stage1(new_id);
        new_id = stage2(new_id);
        new_id = stage3(new_id);
        new_id = stage4(new_id);
        new_id = stage5(new_id);
        new_id = stage6(new_id);
        new_id = stage7(new_id);
    }
    return new_id;
}