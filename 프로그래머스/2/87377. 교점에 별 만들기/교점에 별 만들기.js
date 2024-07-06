function solution(line) {
    let coords = []; // 교점 좌표를 모아둘 배열
    
    // 출력 시, 사각형의 너비와 높이 값을 위한 변수
    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;
    
    // 이중 for문으로 각 직선 간의 교점을 모두 구하기
    for (let i = 0; i < line.length - 1; i++) {
        const [a, b, c] = line[i];
        for (let j = i + 1; j < line.length; j++) {
            const [d, e, f] = line[j];
            
            if (a * e === b * d) continue; // 두 직선의 기울기가 같으면 평행이므로 교점 없음
            else {
                const x = (f * b - c * e) / (a * e - d * b);
                const y = (a * f - c * d) / (b * d - a * e);
                
                // 교점 좌표를 구하고 정수이면 coords 배열에 추가
                if (Number.isInteger(x) && Number.isInteger(y)) {
                    coords.push([x, y]);
                    
                    // 사각형을 위해 최대 좌표와 최소 좌표 구하기
                    if (x < minX) minX = x;
                    if (y < minY) minY = y;
                    if (x > maxX) maxX = x;
                    if (y > maxY) maxY = y;
                }
            }
        }
    }
    
    if (coords.length === 0) return [];

    // 사각형의 너비와 높이 값
    const width = maxX - minX + 1;
    const height = maxY - minY + 1;
    
    // 최종 출력할 사각형 초기화
    let answer = Array.from({ length: height }, () => '.'.repeat(width));
    
    // 교점에 '*' 찍기
    for (let [x, y] of coords) {
        // 좌표를 사각형 배열상의 인덱스로 변환
        const adjustedX = x - minX;
        const adjustedY = maxY - y;
        
        // 해당 좌표에 '*'을 표시
        answer[adjustedY] = answer[adjustedY].substring(0, adjustedX) + '*' + answer[adjustedY].substring(adjustedX + 1);
    }
    
    return answer;
}
