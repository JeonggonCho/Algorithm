function solution(book_time) {
    const convertMinute = (a) => a[0] * 60 + a[1];
    
    const convertedTime = book_time.map((time) => {
        let start = convertMinute(time[0].split(":").map(Number));
        let end = convertMinute(time[1].split(":").map(Number)) + 10;
        return [start, end];
    });
    
    convertedTime.sort((a, b) => a[0] - b[0]);

    let rooms = [];
    for (let i = 0; i < convertedTime.length; i++) {
        let flag = false;
        for (let j = 0; j < rooms.length; j++) {
            if (rooms[j] <= convertedTime[i][0]) {
                rooms[j] = convertedTime[i][1];
                flag = true;
                break;
            }
        }
        if (!flag) {
            rooms.push(convertedTime[i][1]);
        }
    }
    
    return rooms.length;
}