const fs = require('fs')
const input = fs.readFileSync("./input.txt").toString().trim().split("\n")

const numOfWords = parseInt(input[0])

const words = new Map()
input.slice(1).forEach(word => {
    words.set(word, word.length)
})


const sortedWords = [...words].sort((a, b) => {
    if (a[1] < b[1]) {
        return -1
    } else if (a[1] > b[1]) {
        return 1
    } else if (a[1] === b[1]) {
        return a[0].localeCompare(b[0])
    }
})

for (let i = 0; i < sortedWords.length; i++) {
    console.log(sortedWords[i][0])
}
