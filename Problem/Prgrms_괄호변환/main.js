function checkParen(string) {
    const stack = []
    if (string[0] === ")") {
        return false
    }
    stack.push(string[0])
    for (let i = 1; i < string.length; i++) {
        if (string[i] === ")") {
            if (stack[stack.length - 1] === "(") {
                stack.pop()
            }
        } else {
            stack.push(string[i])
        }
    }
    if (stack.length !== 0) {
        return false
    }
    return true
}

function getCorrectParen(p) {
    if (p === "") {
        return ""
    }

    let openParen = 0
    let closeParen = 0
    let targetIdx = -1
    for (let i = 0; i < p.length; i++) {
        if (p[i] === "(") {
            openParen += 1
        } else if (p[i] === ")") {
            closeParen += 1
        }
        if (openParen === closeParen) {
            targetIdx = i
            break
        }
    }
    const u = p.slice(0, targetIdx + 1)
    const v = p.slice(targetIdx + 1)

    if (checkParen(u)) {
        return u + getCorrectParen(v)
    } else {
        const lastAppend = [...u.slice(1, u.length - 1)].map(char => {
            if (char === "(") {
                return ")"
            } else if (char === ")") {
                return "("
            }
            return char
        })
        return "(" + getCorrectParen(v) + ")" + lastAppend.join("")
    }
}

function solution(p) {
    return getCorrectParen(p)
}

console.log(solution("(()())()"))
console.log(solution(")("))
console.log(solution("()))((()"))
console.log(solution("))()()(("))