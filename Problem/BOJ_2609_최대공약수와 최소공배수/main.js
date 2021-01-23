const fs = require('fs')

function getGCD(num1, num2) {
    const remains = num1 % num2
    if (remains === 0) {
        return num2
    }
    num1 = num2
    num2 = remains
    return getGCD(num1, num2)
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split(" ")
        .map(num => parseInt(num))

    const gcd = getGCD(input[0], input[1])
    console.log(gcd)
    console.log(parseInt((input[0] / gcd) * (input[1] / gcd) * gcd))
}

solution()