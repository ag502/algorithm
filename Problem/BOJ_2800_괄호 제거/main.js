const fs = require('fs')

function permutation(curIdx, parenPos, answer, temp, selectedNum) {
    temp.push(parenPos[curIdx])

    if (temp.length < selectedNum) {
        for (let i = curIdx + 1; i < parenPos.length; i++) {
            permutation(i, parenPos, answer, temp, selectedNum)
        }
    } else if (temp.length === selectedNum) {
        answer.push([...temp])
    }
    temp.pop()
}

function solution() {
    const input = fs.readFileSync("./input.txt").toString().trim()
    const parenStack = []
    const parenPos = []

    for (let i = 0; i < input.length; i++) {
        const curChar = input[i]
        if (curChar === "(") {
            parenStack.push([i, curChar])
        } else if (curChar === ")") {
            const [pos, _] = parenStack.pop()
            parenPos.push([pos, i])
        }
    }

    // console.log(parenPos)
    const answer = []
    for (let i = 0; i < parenPos.length; i++) {
        for (let j = 1; j < parenPos.length; j++) {
            permutation(i, parenPos, answer, [], j)
        }
    }
    const express = new Set()

    express.add([...input].filter(char => {
        if (char !== "(" && char !== ")") {
            return true
        }
        return false
    }).join(''))

    for (let i = 0; i < answer.length; i++) {
        const tempString = [...input]
        for (let j = 0; j < answer[i].length; j++) {
            tempString[answer[i][j][0]] = "#"
            tempString[answer[i][j][1]] = "#"
        }
        express.add(tempString.filter(char => char !== "#").join(''))
    }

    // console.log([...express])
    const arrayExpress = [...express].sort()

    arrayExpress.forEach(elem => console.log(elem))
}

solution()