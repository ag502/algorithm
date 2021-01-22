const fs = require('fs')

function parsingURL(url) {
    const urlRegex = /(http|ftp|gopher)\:\/\/([\w\.\-]+)(?:\:(\d+))?(?:\/([\w\W]+))?/
    const matchedInfo = url.match(urlRegex)

    return matchedInfo.slice(1, 5).map(parsedUrl => {
        if (!parsedUrl) {
            return "<default>"
        }
        return parsedUrl
    })
}

function solution() {
    const input = fs.readFileSync("./input.txt")
        .toString()
        .trim()
        .split("\n")

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