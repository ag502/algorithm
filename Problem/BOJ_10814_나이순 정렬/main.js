const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().split("\n")


const numOfMembers = parseInt(input[0])
const members = input.slice(1).map((member, idx) => {
    const [age, name] = member.split(" ")
    return [idx, parseInt(age), name]
})

members.sort((a, b) => {
    if (a[1] < b[1]) {
        return -1
    } else if (a[1] > b[1]) {
        return 1
    } else if (a[1] === b[1]) {
        return a[0] - b[0]
    }
})

for (let i = 0; i < numOfMembers; i++) {
    console.log(`${members[i][1]} ${members[i][2]}`)
}