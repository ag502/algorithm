const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().split('\n')

const numOfPeople = parseInt(input[0])
const time = input[1].split(" ").map(elem => parseInt(elem)).sort((a, b) => a - b)

let spentTime = 0
const accTime = time.reduce((acc, elem) => {
    spentTime += acc
    acc += elem
    return acc
}, 0)

console.log(spentTime + accTime)