const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim()

const pattern = /^(100+1+|01)+$/

const isContained = pattern.test(input)

if (isContained) {
    console.log("SUBMARINE")
} else {
    console.log("NOISE")
}