const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().trim()

function countCroatiaAlphabet (string) {
    const croatiaAlphabetRegex = /(c=)|(c-)|(dz=)|(d-)|(lj)|(nj)|(s=)|(z=)/g
    const matchList = string.match(croatiaAlphabetRegex)

    const stringLength = string.length

    let numOfCroatiaAlphabet = 0
    if (matchList) {
        numOfCroatiaAlphabet = matchList && matchList.reduce((acc, alphabet) => {
            return acc += alphabet.length
        }, 0)
    }

    console.log(stringLength - numOfCroatiaAlphabet + (!!matchList ? matchList.length : 0))
}

countCroatiaAlphabet(input)