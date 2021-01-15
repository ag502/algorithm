const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n")

const [numOfNums, maxNum] = input[0].split(" ").map(num => parseInt(num))
const numbers = input[1].split(" ").map(num => parseInt(num))

const numberCounter = new Map()
numbers.forEach((num, idx) => {
    if (numberCounter.has(num)) {
        numberCounter.set(num, [numberCounter.get(num)[0], numberCounter.get(num)[1] + 1])
    } else {
        numberCounter.set(num, [idx, 1])
    }
})

numbers.forEach((num, idx) => {
    numbers[idx] = [numberCounter.get(num)[0], numberCounter.get(num)[1], num]
})

numbers.sort((a, b) => {
    if (a[1] === b[1]) {
        return a[0] - b[0]
    }
    return a[1] < b[1] ? 1 : -1
})

let answer = ""
for (let i = 0; i < numbers.length; i++) {
    answer += numbers[i][2].toString() + " "
}

console.log(answer.trim())

