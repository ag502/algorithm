function solution(bridge_length, weight, truck_weights) {
    let answer = 0
    const bridge = []
    bridge.fill(0, 0, bridge_length)

    let time = 1
    let sum = truck_weights[0]
    bridge[bridge_length - 1] = truck_weights.shift()

    while (sum !== 0) {
        time += 1
        sum -= bridge.shift()

        if (truck_weights.length !== 0) {
            const top = truck_weights[0]
            if (sum + top <= weight) {
                sum += top
                bridge.push(truck_weights.shift())
            } else {
                bridge.push(0)
            }
        } else {
            bridge.push(0)
        }
    }
    return answer
}

console.log(solution(2, 10, [7, 4, 5, 6]))