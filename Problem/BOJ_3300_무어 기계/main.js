const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n").map(elem => elem.trim())

const numOfMachines = parseInt(input[0])
const machines = input.slice(1)


for (let i = 0; i < numOfMachines * 2; i += 2) {
    const machine = machines[i]
    const output = machines[i + 1]

    let matchCount = 0
    let matchChar = ''
    for (let i = "A".charCodeAt(0); i <= "Z".charCodeAt(0); i++) {
        const newMachine = machine.replace("_", String.fromCharCode(i))
        const regex = new RegExp(`^${newMachine}$`)

        if (!!output.match(regex)) {
            matchCount += 1
            matchChar = String.fromCharCode(i)
        }
    }

    if (matchCount === 0) {
        console.log("!")
    } else if (matchCount > 1) {
        console.log("_")
    } else {
        console.log(matchChar)
    }
}