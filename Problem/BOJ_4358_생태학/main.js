const fs = require('fs')


function solution() {
    const input = fs.readFileSync("./input.txt").toString().trim().split("\n")
    const trees = new Map()
    const totalTree = input.length

    input.forEach(tree => {
        const curTree = tree.trim()
        if (trees.has(curTree)) {
            trees.set(curTree, trees.get(curTree) + 1)
        } else {
            trees.set(curTree, 1)
        }
    })

    const answer = new Map()
    trees.forEach((num, tree) => {
        const ratio = ((num / totalTree) * 100).toFixed(4)
        answer.set(tree, ratio)
    })

    const arrayAnswer = [...answer].sort()
    arrayAnswer.forEach((treeInfo) => console.log(treeInfo[0] + " " + treeInfo[1]))
}


solution()