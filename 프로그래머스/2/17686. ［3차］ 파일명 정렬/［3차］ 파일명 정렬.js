function solution(files) {
    function divideString(file) {
        let head = "", number = "", tail = "";
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

    files.sort((a, b) => {
        const [headA, numberA, tailA] = divideString(a);
        const [headB, numberB, tailB] = divideString(b);

        if (headA.toLowerCase() !== headB.toLowerCase()) {
            return headA.toLowerCase().localeCompare(headB.toLowerCase());
        } else if (parseInt(numberA) !== parseInt(numberB)) {
            return parseInt(numberA) - parseInt(numberB);
        }
        return 0;
    });

    return files;
}
