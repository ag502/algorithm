const fs = require('fs')

function parsingURL(url) {
    const answer = []

    const protocol = url.match(/^(\w+)\:\/\//)
    answer.push(protocol[1])

    const host = url.match(/^\w+\:\/\/([\w\-\.]+)(?:\:\d+)?(?:[\/\w\-\.\W]+)?$/)
    console.log(host)
    answer.push(host[1])

    const port = url.match(/^\w+\:\/\/(?:[\w\-\.]+)(?:\:(\d+))?(?:[\/\w\-\.\W]+)?$/)
    answer.push(!port[1] ? "<default>" : port[1])

    const path = url.match(/^\w+\:\/\/(?:[\w\-\.]+)(?:\:\d+)?(?:\/([\/\w\-\.\W]+))?$/)
    answer.push(!path[1] ? "<default>" : path[1])

    return answer
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .split("\n")
        .map(elem => elem.trim())

    const numOfUrls = parseInt(input[0])
    input.slice(1).map((url, idx) => {
        const parsedData = parsingURL(url)

        console.log(`URL #${idx + 1}`)
        console.log(`Protocol = ${parsedData[0]}`)
        console.log(`Host     = ${parsedData[1]}`)
        console.log(`Port     = ${parsedData[2]}`)
        console.log(`Path     = ${parsedData[3]}`)

        if (idx !== numOfUrls - 1) {
            console.log()
        }
    })
}

solution()