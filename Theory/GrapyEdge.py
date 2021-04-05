graph = {
    0: [1, 4, 5, 6],
    1: [2],
    2: [0],
    3: [],
    4: [2],
    5: [3, 6],
    6: [3]
}

discover = [-1] * 7
finish = [False] * 7
count = 0


def dfs(cur_vertex):
    global count
    count += 1
    discover[cur_vertex] = count

    for next_vertex in graph[cur_vertex]:
        print("{}---{}".format(cur_vertex, next_vertex))
        if discover[next_vertex] == -1:
            print("___Tree Edge___")
            dfs(next_vertex)
        elif discover[cur_vertex] < discover[next_vertex]:
            print("___Forward Edge___")
        elif not finish[next_vertex]:
            print("___Back Edge___")
        else:
            print("___Cross Edge___")
    finish[cur_vertex] = True


def main():
    for vertex in range(0, 7):
        if discover[vertex] == -1:
            dfs(vertex)

    print(discover)


if __name__ == '__main__':
    main()