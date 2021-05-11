const fs = require('fs')

function solution() {
    const input = fs.readFileSync("./input.txt").toString().trim()

    const board = []
    let flag = false
    let count = 0
    let temp = ''
    for (let i = 0; i < input.length; i++) {
        if (input[i] === "X") {
            if (flag) {
                board.push(count)
                temp = ''
                count = 0
                flag = false
            }
            temp += input[i]
        } else if (input[i] === ".") {
            if (!flag && temp !== "") {
                board.push(temp)
                temp = ""
            }
            flag = true
            count += 1
        }
    }
    if (temp !== "") {
        board.push(temp)
    }
    if (count !== 0) {
        board.push(count)
    }

    for (let i = 0; i < board.length; i++) {
        if (typeof board[i] === 'number') {
            board[i] = ".".repeat(board[i])
        } else {
            if (board[i].length % 2 !== 0) {
                console.log(-1)
                return
            } else {
                const aCount = Math.floor(board[i].length / 4)
                const bCount = Math.floor((board[i].length % 4) / 2)
                board[i] = 'AAAA'.repeat(aCount) + 'BB'.repeat(bCount)
            }
        }
    }
    console.log(board.join(''))
}

solution()