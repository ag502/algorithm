function sort(a, b) {
    if (a[1] < b[1]) {
        return 1
    } else if (a[1] > b[1]) {
        return -1
    } else {
        if (a[0] < b[0]) {
            return -1
        }
        return 0
    }
}

function solution(N, stages) {
    const answer = [];

    const counter = new Array(N + 2).fill(0)
    stages.forEach(stage => {
        counter[stage] = counter[stage] + 1
    })

    for (let i = 1; i <= N; i++) {
        let totalReachedPlayer = 0
        for (let j = i; j <= N + 1; j++) {
            totalReachedPlayer += counter[j]
        }
        if (totalReachedPlayer === 0) {
            answer.push([i, 0])
        } else {
            answer.push([i, counter[i] / totalReachedPlayer])
        }
    }
    answer.sort(sort)
    return answer.map(([stage, failRate]) => stage)
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
console.log(solution(4, [4,4,4,4,4]))