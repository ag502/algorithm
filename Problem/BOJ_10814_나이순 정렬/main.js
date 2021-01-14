const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().split("\n")

const numOfMembers = parseInt(input[0])
const members = input.slice(1).map((member, idx) => {
    const [age, name] = member.split(" ")
    return [idx, parseInt(age), name]
})

// console.log(members)

members.sort((a, b) => {
    if (a[1] < b[1]) {
        return -1
    } else if (a[1] > b[1]) {
        return 1
    } else {
        if (a[0] < b[0]) {
            return -1
        } else if (a[0] > b[0]) {
            return 1
        }
    }
})

members.forEach(([idx, age, name]) => {
    console.log(`${age} ${name}`)
})