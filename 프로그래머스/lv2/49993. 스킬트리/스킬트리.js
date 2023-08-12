function solution(skill, skill_trees) {
    var answer = 0;
    const skillArr = skill.split("");
    for (const i of skill_trees) {
        var treesArr = i.split("");
        var inSkill = [];
        for (const j of treesArr) {
            if (skillArr.includes(j)) {
                inSkill.push(j);
            }
        }
        var result = inSkill.join("");
        if (skill.startsWith(result)) {
            answer++;
        }
    }
    return answer;
}