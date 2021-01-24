const fs = require('fs')

function checkBoard(board, rows, cols, curRow, curCol) {
    const curBlock = board[curRow][curCol]
    const movingDir = [[0, 1], [1, 0]]

    let isCorrect = true
    movingDir.forEach(([row, col]) => {
        const [nextRow, nextCol] = [curRow + row, curCol + col]
        if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
            if (curBlock === board[nextRow][nextCol]) {
                isCorrect = false
            }
        } else if (0 <= nextRow && nextRow < rows) {
            if (curBlock === board[nextRow][curCol]) {
                isCorrect = false
            }
        } else if (0 <= nextCol && nextCol < cols) {
            if (curBlock === board[curRow][nextCol]) {
                isCorrect = false
            }
        }
    })
    return isCorrect
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split("\n")
        .map(elem => elem.trim())

    const [rows, cols] = input[0].split(" ").map(elem => parseInt(elem))

    const board = []
    input.slice(1).forEach(row => {
        board.push(Array.from(row))
    })

    let answer = Number.MAX_SAFE_INTEGER
    for (let i = 0; i < rows - 7; i++) {
        for (let j = 0; j < cols -7; j++) {
            let temp = 0
            for (let row = i; row < i + 8; row++) {
                for (let col = j; col < j + 8; col++ ) {
                    if (!checkBoard(board, rows, cols, row, col)) {
                        temp += 1
                    }
                }
            }
            answer = Math.min(answer, temp)
        }
    }
    console.log(answer)
}

solution()