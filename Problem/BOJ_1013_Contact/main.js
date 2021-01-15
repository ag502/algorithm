const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n")

const [numOfSignals, ...signals] = input

const pattern = /^(100+?1+?|01)+$/g

signals.forEach(signal => {
    const result = signal.match(pattern)

    if (!result) {
        console.log('NO')
    } else {
        console.log('YES')
    }
})