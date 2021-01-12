const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().split("\n")

const numOfLopes = parseInt(input[0])
const lopes = input.slice(1).map(length => parseInt(length)).sort((a, b) => b - a)

let maxWeight = lopes[0]

lopes.forEach((lope, idx) => {
    const temp = lope * (idx + 1)
    if (maxWeight < temp) {
        maxWeight = temp
    }
})

console.log(maxWeight)


