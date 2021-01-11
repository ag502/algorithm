const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().split("\n")

const [numOfCoins, targetMoney] = input[0].split(" ").map(elem => parseInt(elem))
const coins = input.slice(1)
    .map(elem => parseInt(elem))
    .filter(elem => targetMoney >= elem)
    .sort((a, b) => b - a)

let numOfUsedCoins = 0
let curRemain = targetMoney

coins.some(coin => {
    if (curRemain === 0) {
        return true
    }
    const temp = parseInt(curRemain / coin)
    numOfUsedCoins += temp
    curRemain -= coin * temp
    return false
})

console.log(numOfUsedCoins)
