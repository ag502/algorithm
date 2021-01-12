const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().split('\n')

const numOfPeople = parseInt(input[0])
const time = input[1].split(" ").map(elem => parseInt(elem)).sort((a, b) => a - b)

let spentTime = 0
let acc = 0
time.forEach(elem => {
    acc += elem
    spentTime += acc
})

console.log(spentTime)