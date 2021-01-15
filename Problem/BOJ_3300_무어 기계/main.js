const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n")

const numOfMachines = parseInt(input[0])
const machines = input.slice(1)

function parsingMachine (machine) {
    let newMachine = ""
    Array.from(machine.trim()).forEach(char => {
        if (char === "(") {
            newMachine += char
            newMachine += "?:"
        } else if (char === "_") {
            newMachine += "([A-Z])"
        } else {
            newMachine += char
        }
    })
    return newMachine
}

for (let i = 0; i < numOfMachines * 2; i += 2) {
    const machine = machines[i]
    const output = machines[i + 1]

    const newMachine = parsingMachine(machine)
    // console.log(newMachine)

    const regex = new RegExp(newMachine)
    if (!regex.test(output)) {
        console.log("!")
    } else {
        const matchInfo = output.match(regex)
        // console.log(matchInfo)

        if (!matchInfo[1]) {
            console.log("_")
        } else {
            console.log(matchInfo[1])
        }
    }
}