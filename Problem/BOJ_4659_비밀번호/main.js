const fs = require('fs')

function checkPassword(password) {
    const checkVowel = /[aeiou]+/
    const tripleWord = /[aeiou]{3}|[bcdfghjklmnpqrstvwxyz]{3}/
    const doubleWord = /aa|bb|cc|dd|ff|gg|hh|ii|jj|kk|ll|mm|nn|pp|qq|rr|ss|tt|uu|vv|ww|xx|yy|zz/

    if (!checkVowel.test(password)) {
        return false
    }
    if (tripleWord.test(password)) {
        return false
    }
    if (doubleWord.test(password)) {
        return false
    }
    return true
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split("\n")
        .map(elem => elem.trim())

    for (let i = 0; i < input.length; i++) {
        if (input[i] === 'end') {
            break
        }
        if (checkPassword(input[i])) {
            console.log(`<${input[i]}> is acceptable.`)
        } else {
            console.log(`<${input[i]}> is not acceptable.`)
        }
    }
}

solution()