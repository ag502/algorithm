const checkDir = [[0, 1], [1, 0], [1, 1]]

function checkBlock(board, rows, cols, curRow, curCol) {
    const curBlock = board[curRow][curCol]
    let deletedBlock = 1
    checkDir.forEach(([movingRow, movingCol]) => {
        const [nextRow, nextCol] = [curRow + movingRow, curCol + movingCol]
        if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
            if (board[nextRow][nextCol] === curBlock && board[nextRow][nextCol] !== "0") {
                deletedBlock += 1
            }
        }
    })
    return deletedBlock === 4
}

function movingBoard(board, rows, cols) {
    for (let col = 0; col < cols; col++) {
        let newCol = []
        for (let row = 0; row < rows; row++) {
            if (board[row][col] !== "0") {
                newCol.push(board[row][col])
            }
        }
        newCol = [...new Array(rows - newCol.length).fill("0"), ...newCol]
        for (let row = 0; row < rows; row++) {
            board[row][col] = newCol[row]
        }
    }
}

function solution(m, n, board) {
    board = board.map(row => (
        [...row]
    ))

    let answer = 0
    while (true) {
        let hasDeletedBlock = false
        const pos = []
        for (let row = 0; row < m; row++) {
            for (let col = 0; col < n; col++) {
                if (checkBlock(board, m, n, row, col)) {
                    pos.push([row, col])
                    pos.push([row, col + 1])
                    pos.push([row + 1, col])
                    pos.push([row + 1, col + 1])
                    hasDeletedBlock = true
                }
            }
        }
        if (!hasDeletedBlock) {
            break
        }
        pos.forEach(([row, col]) => {
            if (board[row][col] !== "0") {
                board[row][col] = "0"
                answer += 1
            }
        })
        movingBoard(board, m, n)
    }
    return answer
}

console.log(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
console.log(solution(6, 6, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))