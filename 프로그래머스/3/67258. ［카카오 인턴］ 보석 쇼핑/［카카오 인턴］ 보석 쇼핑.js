function solution(gems) {    
    let gemTypes = new Set(gems).size; // 모든 종류의 보석 개수
    let l = 0, r = 0; // 왼쪽 인덱스, 오른쪽 인덱스 투포인터를 각각 0으로 설정
    let minRange = [0, gems.length - 1]; // 전체 범위를 최소 범위로 설정
    let gemMap = new Map();
    
    gemMap.set(gems[0], 1);
    
    while (r < gems.length) {
        if (gemMap.size === gemTypes) { // gemMap에 있는 보석 수와 모든 보석 개수가 같다면,
            if ((r - l) < (minRange[1] - minRange[0])) { // 최소 범위보다 현재 범위가 짧다면,
                minRange = [l, r]; // 현재 범위를 최소 범위로 초기화
            }
            
            gemMap.set(gems[l], gemMap.get(gems[l]) - 1); // 왼쪽 인덱스의 보석을 줄이고,
            if (gemMap.get(gems[l]) === 0) { // 개수가 0개 이면 삭제
                gemMap.delete(gems[l]);
            }
            l++; // 왼쪽 인덱스 오른쪽으로 한 칸 이동
        } else { // getMap에 있는 보석 수와 모든 보석 개수가 다른면,
            r++; // 오른쪽 인덱스를 오른쪽으로 한 칸 이동
            if (r < gems.length) { // 오른쪽 인덱스가 전체 배열 길이보다 작은 경우,
                gemMap.set(gems[r], (gemMap.get(gems[r]) || 0) + 1); // 기존에 있는 보석이면 1더하고, 추가된 경우 1
            }
        }
    }
    return [minRange[0] + 1, minRange[1] + 1]; // 최소 범위의 인덱스에 각각 1씩 더하기
}