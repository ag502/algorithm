const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n").map(elem => elem.trim())

const romanNum2Num = new Map(
    [
        ["I", 1],
        ["V", 5],
        ["X", 10],
        ["L", 50],
        ["C", 100],
        ["D", 500],
        ["M", 1000],
        ["IV", 4],
        ["IX", 9],
        ["XL", 40],
        ["XC", 90],
        ["CD", 400],
        ["CM", 900]
    ]
)

const num2RomanNum = new Map(
    [
        [1, "I"],
        [5, "V"],
        [10, "X"],
        [50, "L"],
        [100, "C"],
        [500, "D"],
        [1000, "M"],
        [4, "IV"],
        [9, "IX"],
        [40, "XL"],
        [90, "XC"],
        [400, "CD"],
        [900, "CM"]
    ]
)

function convertRomanNum (romanNumber) {
    let index = 0
    let totalNumber = 0
    while (index < romanNumber.length) {
        if (index !== romanNumber.length - 1) {
            if (romanNumber[index] === "I") {
                if (romanNumber[index + 1] === "V" || romanNumber[index + 1] === "X") {
                    totalNumber += romanNum2Num.get(romanNumber[index] + romanNumber[index + 1])
                    index += 2
                    continue
                }
            } else if (romanNumber[index] === "X") {
                if (romanNumber[index + 1] === "L" || romanNumber[index + 1] === "C") {
                    totalNumber += romanNum2Num.get(romanNumber[index] + romanNumber[index + 1])
                    index += 2
                    continue
                }
            } else if (romanNumber[index] === "C") {
                if (romanNumber[index + 1] === "D" || romanNumber[index + 1] === "M") {
                    totalNumber += romanNum2Num.get(romanNumber[index] + romanNumber[index + 1])
                    index += 2
                    continue
                }
            }
            totalNumber += romanNum2Num.get(romanNumber[index])
            index += 1
        } else {
            totalNumber += romanNum2Num.get(romanNumber[index])
            index += 1
        }
    }
    return totalNumber
}

function convertNum (number) {
    const numbers = [1000, 500, 100, 50, 10, 5, 1, 4, 9, 40, 90, 400, 900]
    numbers.sort((a, b) => b - a)

    const answer = []
    while (number !== 0) {
        numbers.forEach(num => {
            const temp = parseInt(number / num)
            for (let i = 0; i < temp; i++) {
                answer.push(num2RomanNum.get(num))
            }
            number -= num * temp
        })
    }
    return answer.join("")
}

let result = 0
input.forEach(romanNumber => {
    result += convertRomanNum(romanNumber)
})

console.log(result)
console.log(convertNum(result))