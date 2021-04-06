from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 4)

stdin = open("./input.txt", "r")
num_of_friends, num_of_relations = map(int, stdin.readline().split())
graph = {}
answer = 0

for person in range(num_of_friends):
    graph[person] = []

for _ in range(num_of_relations):
    start, finish = map(int, stdin.readline().split())
    graph[start].append(finish)
    graph[finish].append(start)


def dfs(cur_person, visited, depth):
    visited[cur_person] = True
    global answer

    for next_person in graph[cur_person]:
        if not visited[next_person]:
            dfs(next_person, visited, depth + 1)
        if answer == 1:
            return
    visited[cur_person] = False

    if depth >= 5:
        answer = 1
        return


def main():
    for friend in range(num_of_friends):
        visited = [False] * num_of_friends
        dfs(friend, visited, 1)
        if answer == 1:
            print(answer)
            return
    print(answer)


if __name__ == '__main__':
    main()