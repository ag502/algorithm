from sys import stdin


def main():
    N = int(stdin.readline().rstrip())

    visited = [0] * 10

    decreasing_num_list = []

    for i in range(1, 11):
        for j in range(10):
            get_decreasing_num(j, i, 0, visited, decreasing_num_list, [])

    if len(decreasing_num_list) < N:
        print(-1)
    else:
        print(decreasing_num_list[N - 1])


def get_decreasing_num(cur_digit, m, selected_num, visited, decreasing_num_list, answer):
    # 1. 체크인
    visited[cur_digit] = True
    selected_num += 1
    # 2. 목적지
    answer.append(str(cur_digit))
    # 3. 가능성 있는 숫자 순회
    for next_digit in range(0, cur_digit):
        # 4. 갈 수 있는지 검사
        if selected_num != m and not visited[next_digit]:
            get_decreasing_num(next_digit, m, selected_num,
                               visited, decreasing_num_list, answer)
    # 5. 체크아웃
    if len(answer) == m:
        decreasing_num_list.append(int(''.join(answer)))
    answer.pop()
    selected_num -= 1
    visited[cur_digit] = False


if __name__ == "__main__":
    main()
