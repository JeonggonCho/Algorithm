function solution(n, stations, w) {
    const coverage = 2 * w + 1; // 한 기지국이 커버하는 범위
    let answer = 0;
    let idx = 0; // 기지국을 설치할 위치를 나타내는 변수

    for (let station of stations) {
        const start = station - w - 1; // 기지국 왼쪽 범위 시작 위치
        const end = station + w - 1;   // 기지국 오른쪽 범위 끝 위치

        // 기지국 왼쪽 범위까지 커버되지 않은 부분 계산
        answer += Math.ceil((start - idx) / coverage);
        idx = end + 1; // 다음 기지국 설치 위치 갱신
    }

    // 마지막 기지국 이후 남은 부분 계산
    answer += Math.ceil((n - idx) / coverage);

    return answer;
}