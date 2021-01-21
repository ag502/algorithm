const fs = require('fs')

function processString(string) {
    let answer = ''
    answer = string.replace(/\s+/g, " ")
        .replace(/^\s/g, "")
        .replace(/\s$/g, "")
        .replace(/[\(\[\{]/g, "(")
        .replace(/[\)\]\}]/g, ")")
        .replace(/;/g, ",")
        .replace(/\s*([\(\)\.\,\;\:])\s*/g, "$1")

    return answer
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split("\n")
        .map(elem => elem.trim())

    const testCase = parseInt(input[0])
    const stringList = input.slice(1)
    for (let i = 0; i < testCase; i++) {
        const data1 = stringList[i * 2].toLowerCase()
        const data2 = stringList[i * 2 + 1].toLowerCase()

        if (processString(data1) === processString(data2)) {
            console.log(`Data Set ${i + 1}: equal`)
        } else {
            console.log(`Data Set ${i + 1}: not equal`)
        }
        if (i !== testCase - 1) {
            console.log()
        }

    }
}

solution()