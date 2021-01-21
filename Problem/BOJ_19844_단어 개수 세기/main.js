const fs = require('fs')

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .trim()

    const replacedString = input
        .replace(/-/g, " ")
        .split(" ")

    let answer = []
    replacedString.forEach(word => {
        const array = word.replace(/^(c|j|n|m|t|s|l|d|qu|s)'([aeiouh])/g, "$1 $2").split(" ")
        answer = [...answer, ...array]
    })
    console.log(answer.length)
}

solution()