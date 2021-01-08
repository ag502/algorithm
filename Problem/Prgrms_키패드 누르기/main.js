const keypadPos = {
    "1": [0, 0],
    "2": [0, 1],
    "3": [0, 2],
    "4": [1, 0],
    "5": [1, 1],
    "6": [1, 2],
    "7": [2, 0],
    "8": [2, 1],
    "9": [2, 2],
    "*": [3, 0],
    "0": [3, 1],
    "#": [3, 2]
}

const movingDir = [[-1, 0], [0, 1], [1, 0], [0, -1]]

function calShortestDist(keypads, start, end) {
    const queue = []
    const visited = [[false, false, false], [false, false, false], [false, false, false], [false, false, false]]
    queue.push(start)

    let distance = 0
    while (queue.length != 0) {
        const size = queue.length
        for (let i = 0; i < size; i++) {
            const [curRow, curCol] = queue.shift()
            if (curRow === end[0] && curCol === end[1]) {
                return distance
            }
            movingDir.forEach(([movingRow, movingCol]) => {
                const [nextRow, nextCol] = [curRow + movingRow, curCol + movingCol]
                if ((0 <= nextRow && nextRow < keypads.length) && (0 <= nextCol && nextCol < keypads[0].length)) {
                    if (!visited[nextRow][nextCol]) {
                        visited[nextRow][nextCol] = true
                        queue.push([nextRow, nextCol])
                    }
                }
            })
        }
        distance += 1
    }
}

function solution(numbers, hand) {
    const keypads = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"], ["*", "0", "#"]]
    const result = []
    let curLeft = "*"
    let curRight = "#"
    numbers.forEach((number) => {
        const stringNum = number.toString()
        if (["1", "4", "7"].includes(stringNum)) {
            result.push('L')
            curLeft = stringNum
        } else if (["3", "6", "9"].includes(stringNum)) {
            result.push('R')
            curRight = stringNum
        } else {
            const leftDist = calShortestDist(keypads, keypadPos[curLeft], keypadPos[stringNum])
            const rightDist = calShortestDist(keypads, keypadPos[curRight], keypadPos[stringNum])
            if (leftDist < rightDist) {
                result.push('L')
                curLeft = stringNum
            } else if (leftDist > rightDist) {
                result.push('R')
                curRight = stringNum
            } else {
                if (hand === "right") {
                    result.push('R')
                    curRight = stringNum
                } else {
                    result.push('L')
                    curLeft = stringNum
                }
            }
        }
    })
    return result.join('')
}

console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))