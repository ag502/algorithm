from sys import stdin

stdin = open("./input.txt", "r")
num_of_str = int(stdin.readline())

char_list = []
word_list = set()


def dfs(cur_idx, visited, temp, cur_string_length):
    visited[cur_idx] = True
    temp.append(char_list[cur_idx])
    cur_str = ''.join(temp)

    for next_idx in range(len(char_list)):
        flag = True
        if len(cur_str) == cur_string_length - 1:
            if cur_str + char_list[next_idx] in word_list:
                flag = False
        if flag and not visited[next_idx] and len(cur_str) != cur_string_length:
            dfs(next_idx, visited, temp, cur_string_length)

    if len(cur_str) == cur_string_length:
        word_list.add(cur_str)

    temp.pop()
    visited[cur_idx] = False


def main():
    for _ in range(num_of_str):
        char_list.clear()
        string = list(stdin.readline().rstrip())
        for char in string:
            char_list.append(char)

        char_list.sort()
        cur_string_length = len(string)

        for idx, char in enumerate(char_list):
            visited = [False] * len(char_list)
            if char not in word_list and not visited[idx]:
                dfs(idx, visited, [], cur_string_length)

    word_list_list = list(word_list)
    word_list_list.sort(key=lambda x: (len(x), x))

    for string in word_list_list:
        print(string)


if __name__ == '__main__':
    main()