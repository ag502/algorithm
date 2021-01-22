const fs = require('fs')

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .trim()

    const parsedString = input.replace(";", "")
        .split(/[\s,]/g)
        .filter(string => string !== "")

    const commonVariableType = parsedString[0]
    parsedString.slice(1).forEach(variable => {
        const matchedInfo = variable.match(/([a-zA-Z]+)([\*\[\]&]+)?/)
        // console.log(matchedInfo)
        const variableName = matchedInfo[1]
        const variableType = !matchedInfo[2] ? "" : matchedInfo[2].replace(/(\[)(\])/g, "$2$1")

        console.log(`${commonVariableType}${[...variableType].reverse().join("")} ${variableName};`)
    })
}

solution()