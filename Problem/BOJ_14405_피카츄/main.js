const fs = require('fs')

function solution() {
    const input = fs.readFileSync("./input.txt").toString().trim()

    const replacedString = input
        .replace(/pi/g, "**")
        .replace(/ka/g, "**")
        .replace(/chu/g, "***")

    const matchedString = replacedString.match(/\*/g)

    if (!matchedString || input.length !== matchedString.length) {
        console.log("NO")
    } else {
        console.log("YES")
    }
}

solution()