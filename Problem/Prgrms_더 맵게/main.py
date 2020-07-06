import heapq as hq

def get_scoville(food1, food2):
    return food1 + (food2 * 2)

def update_scoville(scoville_list):
    food1 = hq.heappop(scoville_list)
    food2 = hq.heappop(scoville_list)
    hq.heappush(scoville_list, get_scoville(food1, food2))

def check_scoville(scoville_list, K):
    if scoville_list[0] >= K:
        return True
    return False

def solution(scoville, K):
    answer = 0
    hq.heapify(scoville)

    while True:
        if check_scoville(scoville, K):
            return answer
        if len(scoville) == 1:
            return -1
        else:
            update_scoville(scoville)
            answer += 1

            