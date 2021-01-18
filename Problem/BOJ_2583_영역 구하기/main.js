const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().split('\n')

const [rows, cols, numOfSquares] = input[0].split(" ").map(elem => parseInt(elem))

const movingDir = [[-1, 0], [1, 0], [0, -1], [0, 1]]

const graphSquare = Array.from(Array(rows), () => Array(cols).fill(0))
input.slice(1).forEach(positions => {
    const [x1, y1, x2, y2] = positions.split(" ").map(elem => parseInt(elem))
    for (let i = rows - y2; i < rows - y1; i++) {
        for (let j = x1; j < x2; j++) {
            graphSquare[i][j] = 1
        }
    }
})


function dfs(graphPaper, rows, cols, curRow, curCol, areas) {
    graphPaper[curRow][curCol] = -1

    for (let i = 0; i < movingDir.length; i++) {
        const [nextRow, nextCol] = [curRow + movingDir[i][0], curCol + movingDir[i][1]]
        if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
            if (graphPaper[nextRow][nextCol] === 0) {
                areas = dfs(graphPaper, rows, cols, nextRow, nextCol, areas) + 1
            }
        }
    }
    return areas
}

let numOfAreas = 0
const areaList = []
for (let row = 0; row < rows; row++) {
    for (let col = 0; col < cols; col++) {
        if (graphSquare[row][col] === 0) {
            numOfAreas += 1
            areaList.push(dfs(graphSquare, rows, cols, row, col, 1))
        }
    }
}

console.log(numOfAreas)
console.log(areaList.sort((a, b) => a - b).join(" "))