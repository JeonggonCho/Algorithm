function solution(files) {
    function parseFile(file) {
        let head = '', number = '', tail = '';
        let i = 0;
        
        while (i < file.length && !/\d/.test(file[i])) {
            head += file[i];
            i++;
        }
        
        while (i < file.length && /\d/.test(file[i])) {
            number += file[i];
            i++;
        }
        
        tail = file.slice(i);
        
        return [head, number, tail];
    }

    function compare(a, b) {
        const [headA, numberA, tailA] = parseFile(a);
        const [headB, numberB, tailB] = parseFile(b);
        
        const headCompare = headA.toLowerCase().localeCompare(headB.toLowerCase());
        if (headCompare !== 0) return headCompare;
        
        const numberCompare = parseInt(numberA) - parseInt(numberB);
        if (numberCompare !== 0) return numberCompare;
        
        return 0;
    }

    return files.sort(compare);
}