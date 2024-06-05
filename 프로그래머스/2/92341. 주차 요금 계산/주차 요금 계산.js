function solution(fees, records) {
    var answer = [];
    const maxMinTime = 23 * 60 + 59; // 23시 59분을 분으로 환산
    const [defaultTime, defaultFee, unitTime, unitFee] = fees; // fees 구조분해할당
    const data = new Object(); // 차번호(키) 분(값) 데이터를 담을 빈 객체 생성
    
    for (let i = 0; i < records.length; i++) {
        const record = records[i].split(' '); // record를 띄워쓰기 기준으로 배열화
        const [time, carNumber, behavior] = record; // record 구조분해할당
        
        const [hour, min] = time.split(":"); // 시간을 시, 분으로 분리
        const minTime = parseInt(hour) * 60 + parseInt(min); // 시간 분으로 환산
        
        // data 객체에 키(차번호) 값(분)으로 담기
        if (data[carNumber] === undefined) {
            data[carNumber] = [];
        } data[carNumber].push(minTime);
    }
    
    const results = new Array(); // 차번호와 주차한 총 시간을 담을 배열
    
    // 최종적으로 출차 기록이 없으면(시간 기록이 홀수개) 23시 59분 넣고 총 주차시간 계산
    for (let j in data) {
        let totalParkingTime = 0;
        let totalFee = 0;
        
        if (data[j].length % 2 !== 0) {
            data[j].push(maxMinTime);    
        } 
        
        for (let k = 0; k < data[j].length / 2; k++) {
            totalParkingTime += (data[j][2 * k + 1] - data[j][k * 2]);
        }
        
        if (totalParkingTime <= defaultTime ) {
            results.push ({carNumber: j, fee: defaultFee});
        } else {
            totalFee = defaultFee + Math.ceil((totalParkingTime - defaultTime) / unitTime) * unitFee;
            results.push ({carNumber: j, fee: totalFee});
        }
    }
    
    // 차 번호 낮은 순으로 정렬
    results.sort((a, b) => parseInt(a.carNumber) - parseInt(b.carNumber));
    
    // 순회하면서 요금만 answer에 넣기
    for (let l of results) {
        answer.push(l.fee);
    }
    
    return answer;
}