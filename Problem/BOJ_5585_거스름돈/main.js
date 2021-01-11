const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString()

const cost = parseInt(input)
const coins = [500, 100, 50, 10, 5, 1]
let remain = 1000 - cost

let numOfCoins = 0
coins.some(coin => {
    if (remain === 0) {
        return true
    }
    numOfCoins += parseInt(remain / coin)
    remain = remain - coin * parseInt(remain / coin)
    return false
})

console.log(numOfCoins)
