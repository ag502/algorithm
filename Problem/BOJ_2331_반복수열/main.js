const fs = require('fs')

function generateNextSeq (prevNumber, p) {
    let nextNumber = 0
    Array.from(prevNumber.toString()).forEach(digit => {
        nextNumber += parseInt(digit) ** p
    })
    return nextNumber
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split(" ")
        .map(elem => parseInt(elem))

    const counter = new Map()
    counter.set(input[0], 0)

    const sequence = [input[0]]
    let curIdx = 1
    while (true) {
        const nextNumber = generateNextSeq(sequence[curIdx - 1], input[1])
        sequence.push(nextNumber)
        if (counter.has(nextNumber)) {
            console.log(counter.get(nextNumber))
            return
        } else {
            counter.set(nextNumber, curIdx)
        }
        curIdx += 1
    }
}

solution()