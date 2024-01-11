function solution(friends, gifts) {
    const records = {};
    const giveTake = {};
    const currentMonthRecord = {}
    friends.forEach((friend) => {
        records[friend] = [0, 0, 0];
        giveTake[friend] = [];
        currentMonthRecord[friend] = 0;
    })
    
    gifts.forEach((gift) => {
        const people = gift.split(" ");
        records[people[0]][0]++;
        records[people[1]][1]++;
        giveTake[people[0]].push(people[1]);
    })
    
    friends.forEach((friend) => {
        records[friend][2] = records[friend][0] - records[friend][1];
    })
    
    for (let i = 0; i < friends.length - 1; i++) {
        for (let j = i + 1; j < friends.length; j++) {
            if (giveTake[friends[i]].includes(friends[j]) || giveTake[friends[j]].includes(friends[i])) {
                let cnt1 = giveTake[friends[i]].filter(el => el === friends[j]).length;
                let cnt2 = giveTake[friends[j]].filter(el => el === friends[i]).length;
                if (cnt1 > cnt2) {
                    currentMonthRecord[friends[i]]++;
                } else if (cnt1 < cnt2) {
                    currentMonthRecord[friends[j]]++;
                } else {
                    if (records[friends[i]][2] > records[friends[j]][2]) {
                        currentMonthRecord[friends[i]]++;
                    } else if (records[friends[i]][2] < records[friends[j]][2]) {
                        currentMonthRecord[friends[j]]++;
                    }
                }
            } else {
                if (records[friends[i]][2] > records[friends[j]][2]) {
                    currentMonthRecord[friends[i]]++;
                } else if (records[friends[i]][2] < records[friends[j]][2]) {
                    currentMonthRecord[friends[j]]++;
                }
            }
        }
    }
    let answer = Math.max(...Object.values(currentMonthRecord));
    return answer;
}