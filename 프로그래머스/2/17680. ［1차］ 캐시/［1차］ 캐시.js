function solution(cacheSize, cities) {
    let answer = 0;
    let cache = [];
    
    // 캐시사이즈가 0일 경우, 모든 도시이름에서 캐시미스 발생
    if (cacheSize === 0) return cities.length * 5;
    
    // 캐시사이즈가 0이 아닌 경우,
    for (let i = 0; i < cities.length; i++) {
        let city = cities[i].toLowerCase();
        let idx = cache.indexOf(city);
        
        // 캐시에 city가 있는 경우,
        if (idx !== -1) {
            answer++; // 실행시간에 1 더하기
            cache.splice(idx, 1); // 해당 인덱스의 city 제거
            cache.push(city); // 다시 캐시에 해당 city 넣기
        } else { // 캐시에 city가 없는 경우
            answer += 5; //실행시간에 5 더하기
            // 만약 캐시가 가득 차있으면, 가장 오래된 캐시 제거
            if (cache.length === cacheSize) cache.shift();
            cache.push(city); // 최근 city 넣기
        }
    }
    return answer;
}