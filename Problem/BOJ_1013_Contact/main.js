const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().split("\n").map(elem => elem.trim())

const [numOfSignals, ...signals] = input

const pattern = /(100+?1+?|01)+/g

signals.forEach(signal => {
    const result = pattern.exec(signal)
    // console.log(result)

    if (!result) {
        console.log('NO')
    } else {
        if (result[0] === signal) {
            console.log('YES')
        } else {
            console.log('NO')
        }
    }
})