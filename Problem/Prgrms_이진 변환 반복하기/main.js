function convertBinary(s) {
    const binaryTemp = /0/g
    let numOfZero = 0

    if (s.search(binaryTemp) !== -1) {
        numOfZero = s.match(binaryTemp).length
        s = s.replace(binaryTemp, "")
    }
    const binaryNumber = s.length.toString(2)
    return [numOfZero, binaryNumber]
}

function solution(s) {
    let numOfZero = 0
    let count = 0
    while (true) {
        let [curNumOfZero, convertedNum] = convertBinary(s)
        count += 1
        numOfZero += curNumOfZero
        s = convertedNum

        if (s === "1") {
            break
        }
    }
    return [count, numOfZero]
}

console.log(solution("110010101001"))
console.log(solution("01110"))
console.log(solution("1111111"))