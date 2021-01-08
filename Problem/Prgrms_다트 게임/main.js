const bonusArea = (type, score) => {
    switch (type) {
        case "S":
            return score
        case "D":
            return score ** 2
        case "T":
            return score ** 3
    }
}


const calculateScore = (scoreSeq) => {
    const scores = []
    scoreSeq.forEach(score => {
        if (score === "*") {
            if (scores.length === 1) {
                const curScore = scores.pop()
                scores.push(curScore * 2)
            } else {
                const curScore = scores.pop()
                const prevScore = scores.pop()
                scores.push(prevScore * 2)
                scores.push(curScore * 2)
            }
        } else if (score === "#") {
            const curScore = scores.pop()
            scores.push(curScore * (-1))
        } else {
            const scoreNum = parseInt(score)
            const type = score.match(/[S,T,D]/g)[0]
            const calculatedScore = bonusArea(type, scoreNum)
            scores.push(calculatedScore)
        }
    })
    return scores
}

const solution = (dartResult) => {
    const scoreParsingRegex = /(\d[S,D,T]|[#, \*])/g
    const parsingResult = dartResult.replace(scoreParsingRegex, "$1 ").trim().split(" ")
    const scores = calculateScore(parsingResult)
    return scores.reduce((sum, score) => sum += score, 0)
}

console.log(solution("1S2D*3T"))
console.log(solution("1D2S#10S"))
console.log(solution("1D2S0T"))
console.log(solution("1S*2T*3S"))
console.log(solution("1D#2S*3S"))
console.log(solution("1T2D3D#"))
console.log(solution("1D2S3T*"))

