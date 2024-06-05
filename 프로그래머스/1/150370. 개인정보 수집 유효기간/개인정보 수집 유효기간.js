function solution(today, terms, privacies) {
    let answer = [];
    
    const dividedToday = today.split(".").map(x => parseInt(x));
    const dividedTerms = new Object();
    
    for (let i = 0; i < terms.length; i++) {
        const term = terms[i].split(" ");
        dividedTerms[term[0]] = parseInt(term[1]);
    }
    
    for (let j = 0; j < privacies.length; j++) {
        const [date, termType] = privacies[j].split(" ");
        const dividedDate = date.split(".").map(x => parseInt(x));
        
        let year = dividedDate[0];
        let month = dividedDate[1] + dividedTerms[termType];
        let day = dividedDate[2];
        
        year += Math.floor((month - 1) / 12);
        month = (month - 1) % 12 + 1;
        
        if (year < dividedToday[0] 
            || (year === dividedToday[0] && month < dividedToday[1]) 
            || (year === dividedToday[0] && month === dividedToday[1] && day <= dividedToday[2])
           ) {
            answer.push(j + 1);
        }
    }
    return answer;
}