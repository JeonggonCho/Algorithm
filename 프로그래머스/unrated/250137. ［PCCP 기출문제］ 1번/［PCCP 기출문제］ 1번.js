function solution(bandage, health, attacks) {
    const maxHealth = health; // 최대 체력 상수 maxHealth 할당
    const time = attacks[attacks.length-1][0]; // 총 플레이 시간이 마지막 공격받는 시간이므로 상수 time 할당 
    let continuous = 0; // 연속 체력보충 성공여부 확인할 변수 continuous 초기화
    
    for (let i = 0; i <= time; i++) { // 상수 time만큼 순회
        if (attacks[0][0] === i) { // 현재 시간과 공격 시간이 같으면,
            health -= attacks[0][1]; // 체력에서 피해량을 빼고
            attacks.shift(); // attacks배열에서 적용된 공격 삭제
            continuous = 0; // 연속 성공 0으로 초기화
            
            if (health <= 0) { // 공격을 받고 체력이 0이하인 경우,
                return -1; // -1을 리턴
            } 
        } else { // 현재시간과 공격 시간이 다르면,
            if (health < maxHealth) { // 현재 체력이 최대 체력이 아니면,
                health += bandage[1]; // 초당 회복량을 체력에 더한다.
                continuous += 1; // 연속 성공에 1을 더한다.
                if (continuous === bandage[0]) { // 연속 성공과 시전 시간이 같다면,
                    health += bandage[2]; // 체력에 추가 회복량을 더한다.
                    continuous = 0; // 연속 성공 0으로 초기화
                }
                if (health > maxHealth) { // 회복이 이루어진후, 현재 체력이 최대 체력보다 크면,
                    health = maxHealth; // 현재 체력을 최대 체력으로 할당
                }
            }
        }
    }
    return health; // 모든 공격이 끝난 후, 남은 체력을 리턴
}