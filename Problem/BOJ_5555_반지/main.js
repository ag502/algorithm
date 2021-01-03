const fs = require("fs")
// const input = fs.readFileSync("./input.txt").toString().split('\n')
const input = fs.readFileSync("./dev/stdin").toString().split('\n')

const [template, numOfString, ...stringList] = input.map(elem => elem.trim())

const regularExp = new RegExp(`.*${template}.*`)

let answer = 0
stringList.forEach(string => {
    if (regularExp.test(string + string)) {
        answer += 1
    }
})

console.log(answer)