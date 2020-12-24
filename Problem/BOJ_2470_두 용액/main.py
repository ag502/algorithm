from sys import stdin

def lower_bound(array, start_idx, target):
    start = start_idx
    end = len(array) - 1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start

def main():
    stdin = open('./input.txt', 'r')
    num_of_liquids = int(stdin.readline())
    liquids = list(map(int, stdin.readline().split()))

    liquids.sort()

    answer = []
    for idx, liquid in enumerate(liquids):
        target_idx = lower_bound(liquids, idx + 1, -liquid)

        distance = 2 * (10 ** 9) + 1
        answer_idx = -1

        prev_idx = target_idx - 1
        next_idx = target_idx + 1
        if idx < prev_idx < num_of_liquids:
            if distance >= abs(liquids[idx] + liquids[prev_idx]):
                distance = abs(liquids[idx] + liquids[prev_idx])
                answer_idx = prev_idx
        if idx < next_idx < num_of_liquids:
            if distance >= abs(liquids[idx] + liquids[next_idx]):
                distance = min(distance, abs(liquids[idx] + liquids[next_idx]))
                answer_idx = next_idx
        if idx < target_idx < num_of_liquids:
            if distance >= abs(liquids[idx] + liquids[target_idx]):
                distance = min(distance, abs(liquids[idx] + liquids[target_idx]))
                answer_idx = target_idx
        answer.append([distance, liquids[idx], liquids[answer_idx]])

    answer.sort(key=lambda x:(x[0]))
    print(' '.join(map(str, sorted([answer[0][1], answer[0][2]]))))

if __name__ == '__main__':
    main()
