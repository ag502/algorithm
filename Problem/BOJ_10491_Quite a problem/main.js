const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n")

const pattern = /problem/i

input.forEach(sentence => {
    const isContained = pattern.test(sentence)
    if (isContained) {
        console.log("yes")
    } else {
        console.log("no")
    }
})