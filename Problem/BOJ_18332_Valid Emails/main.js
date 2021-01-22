const fs = require('fs')

function checkUserNameValidation(userName) {
    if (/^\./.test(userName) || (/\.$/).test(userName)) {
        return null
    } else if (/\.\./.test(userName)) {
        return null
    }
    const matchedInfo = userName.match(/^[a-zA-Z0-9_\.]+$/g)
    if (!matchedInfo || matchedInfo[0].length !== userName.length) {
        return null
    }

    const removedPeriods = userName.replace(/\./g, "")
    if (removedPeriods.length > 30 || 6 > removedPeriods.length) {
        return null
    }
    return removedPeriods.toLowerCase()
}

function checkDomainNameValidation(domain) {
    if (/^\./.test(domain) || /\.$/.test(domain)) {
        return null
    }
    const partOfDomain = domain.split(".")
    // if (partOfDomain.length === 1) {
    //     return null
    // }
    for (let i = 0; i < partOfDomain.length; i++) {
        const matchedInfo = partOfDomain[i].match(/^[a-zA-Z0-9\-]+$/g)
        if (!matchedInfo || matchedInfo[0] !== partOfDomain[i]) {
            return null
        }
    }
    const parsedDomain = partOfDomain.join(".").toLowerCase()
    // console.log(parsedDomain, parsedDomain.length)
    if (parsedDomain.length < 3 || parsedDomain.length > 30) {
        return null
    }
    return parsedDomain
}

function checkEmailValidation(email) {
    if (email.match(/@/g).length >= 2) {
        return null
    }
    const [userName, domainName] = email.split("@")

    const validUserName = checkUserNameValidation(userName)
    const validDomainName = checkDomainNameValidation(domainName)

    if (!validUserName || !validDomainName) {
        return null
    }
    // console.log(validUserName)
    return `${validUserName}@${validDomainName}`
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split("\n")
        .map(elem => elem.trim())

    const numOfEmails = parseInt(input[0])

    const distinctEmails = new Set()
    input.slice(1).forEach(email => {
        const validEmail = checkEmailValidation(email)
        if (!!validEmail) {
            distinctEmails.add(validEmail)
        }
    })
    console.log(distinctEmails.size)
}

solution()