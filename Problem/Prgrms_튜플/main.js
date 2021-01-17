function solution(s) {
    const answer = []

    const set = JSON.parse(s.replace(/{/g, "[").replace(/}/g, "]"))
    set.sort((a, b) => a.length - b.length)

    answer.push(set[0][0])
    for (let i = 1; i < set.length; i++) {
        let addValue = 0
        set[i].some(number => {
            if (!set[i - 1].includes(number)) {
                addValue = number
                return true
            }
            return false
        })
        answer.push(addValue)
    }
    return answer
}

console.log(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
console.log(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
console.log(solution("{{20,111},{111}}"))
console.log(solution("{{123}}"))
console.log(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))