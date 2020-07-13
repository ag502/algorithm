from collections import deque

def sum_of_array(arr1, arr2):
    for idx, elem in enumerate(arr1):
        arr1[idx] += arr2[idx]

def solution(progresses, speeds):
    answer = []
    progresses_queue = deque(progresses)
    speeds_queue = deque(speeds)

    while progresses_queue:
        distribution_count = 0
        sum_of_array(progresses_queue, speeds_queue)
        while progresses_queue and progresses_queue[0] >= 100:
            progresses_queue.popleft()
            speeds_queue.popleft()
            distribution_count += 1

        if distribution_count != 0:
            answer.append(distribution_count)


    return answer