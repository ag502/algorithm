function checkDuplicateDoll(basket, newDoll) {
    if (basket.length !== 0) {
        const topDoll = basket[basket.length - 1]
        if (topDoll === newDoll) {
            return true
        }
    }
    return false
}

function solution(board, moves) {
    let answer = 0
    const width = board.length
    const basket = []
    moves.forEach(colNum => {
        let curDoll = 0
        for (let rowNum = 0; rowNum < width; rowNum++) {
            if (board[rowNum][colNum - 1] !== 0) {
                curDoll = board[rowNum][colNum - 1]
                board[rowNum][colNum - 1] = 0
                break
            }
        }

        if (curDoll !== 0) {
            if (checkDuplicateDoll(basket, curDoll)) {
                basket.pop()
                answer += 2
            } else {
                basket.push(curDoll)
            }
        }
    })
    return answer
}

console.log(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))