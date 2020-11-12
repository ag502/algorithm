from sys import stdin

def main():
    stdin = open('./test_case.txt', 'r')
    num_of_bead = int(stdin.readline())
    weights = list(map(int, stdin.readline().split()))

    energy_list = []
    for idx in range(1, len(weights) - 1):
        dfs(weights, idx, energy_list, 0, 0)

    print(max(energy_list))

def get_side_weights(cur_idx, weights):
    left_weight = right_weight = 0
    for idx in range(cur_idx - 1, -1, -1):
        if weights[idx] != -1:
            left_weight = weights[idx]
            break
    for idx in range(cur_idx + 1, len(weights)):
        if weights[idx] != -1:
            right_weight = weights[idx]
            break
    return [left_weight, right_weight]

def dfs(weights, cur_idx, energy_list, acc_energy, count):
    # 1. 방문
    cur_weight = weights[cur_idx]
    weights[cur_idx] = -1
    left_weight, right_weight = get_side_weights(cur_idx, weights)
    add_energy = left_weight * right_weight
    acc_energy += add_energy
    count += 1

    # 2. 갈 수 있는 곳 탐색
    for idx in range(1, len(weights) - 1):
        if weights[idx] != -1:
            dfs(weights, idx, energy_list, acc_energy, count)

    # 3. 체크아웃
    if count == len(weights) - 2:
        energy_list.append(acc_energy)
    weights[cur_idx] = cur_weight
    acc_energy -= add_energy
    count -= 1

if __name__ == '__main__':
    main()