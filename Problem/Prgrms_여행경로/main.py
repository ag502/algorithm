def dfs(airports, cur_airport, answer, num_of_tickets, cnt, visited):
    answer.append(cur_airport)
    visited[cur_airport] -= 1
    cnt += 1

    if cur_airport in airports:
        for idx, next_airport in enumerate(airports[cur_airport]):
            # if airports[cur_airport][idx] != -1:
            #     airports[cur_airport][idx] = -1
            #     dfs(airports, next_airport, answer, num_of_tickets, cnt)
            if visited[next_airport] != 0:
                dfs(airports, next_airport, answer, num_of_tickets, cnt, visited)
    else:
        if cnt - 1 != num_of_tickets:
            print(cnt)
            visited[cur_airport] += 1
            answer.pop()

def solution(tickets):
    answer = []
    airport_paths = {}
    visited = {}
    visited_t = {"ICN": 1}


    for depart, arrive in tickets:
        if depart not in airport_paths:
            airport_paths[depart] = []
        airport_paths[depart].append(arrive)

        if arrive not in visited_t:
            visited_t[arrive] = 0
        visited_t[arrive] += 1

        visited[depart + arrive] = False

    for depart in airport_paths.keys():
        airport_paths[depart] = list(airport_paths[depart])
        airport_paths[depart].sort()

    # print(airport_paths)
    # print(visited_t)
    dfs(airport_paths, "ICN", answer, len(tickets), 0, visited_t)
    return answer

print(solution([["ICN", "A"], ["A", "B"], ["B", "A"], ["A", "ICN"], ["ICN", "A"]]))
print(solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]]))
print(solution([["ICN", "A"], ["ICN", "A"], ["A", "ICN"]]))
print(solution( [["ICN", "A"], ["A", "C"], ["A", "D"], ["D", "B"], ["B", "A"]]))
print(solution([["ICN", "JFK"], ["JFK", "ICN"], ["JFK", "ICN"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))
print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"], ["ICN", "HND"], ["HND", "ICN"], ["HND", "JFK"], ["IAD", "HND"]]))