from sys import stdin
from collections import deque


class Main:
    def __init__(self):
        self.operation_length = 0
        self.operation = ''
        self.paren_pos = []
        self.visited = None

        self.main()

    def make_parenthesis(self, cur_num_idx, count, num_idx_list=[]):
        num_idx_list.append(cur_num_idx)
        num_idx_list.append(cur_num_idx + 2)
        self.visited[cur_num_idx] = True
        self.visited[cur_num_idx + 2] = True

        if len(num_idx_list) < count:
            for next_num_idx in range(cur_num_idx + 1, self.operation_length - 2):
                value = self.operation[next_num_idx]
                if value.isdigit() and not self.visited[next_num_idx] and not self.visited[next_num_idx + 2]:
                    self.make_parenthesis(next_num_idx, count, num_idx_list)
        elif len(num_idx_list) == count:
            self.paren_pos.append(num_idx_list[:])

        self.visited[cur_num_idx] = False
        self.visited[cur_num_idx + 2] = False
        num_idx_list.pop()
        num_idx_list.pop()

    def insert_paren(self, paren_pos):
        new_operation = ""
        for idx, char in enumerate(self.operation):
            try:
                pos_idx = paren_pos.index(idx)
                if pos_idx % 2 == 0:
                    new_operation += "("
                    new_operation += char
                else:
                    new_operation += char
                    new_operation += ")"
            except:
                new_operation += char

        return new_operation

    def change_post(self, new_operation):
        post_operation = ''
        stack = deque()

        for char in new_operation:
            if char == "(":
                stack.append(char)
            elif char == ")":
                while True:
                    top = stack.pop()
                    if top == "(":
                        break
                    post_operation += top
            elif char.isdigit():
                post_operation += char
            else:
                if stack and stack[len(stack) - 1] in ["+", "-", "*"]:
                    post_operation += stack.pop()
                stack.append(char)

        while stack:
            post_operation += stack.pop()

        return post_operation

    def do_operation(self, post_op):
        stack = deque()

        for char in post_op:
            if char.isdigit():
                stack.append(char)
            else:
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(str(eval(num_1 + char + num_2)))

        return int(stack.pop())

    def main(self):
        stdin = open("./input.txt", "r")

        self.operation_length = int(stdin.readline())
        self.operation = stdin.readline().rstrip()

        self.visited = [False] * self.operation_length

        for start_idx in range(self.operation_length - 1):
            for count in range(2, (self.operation_length // 2) + 1, 2):
                if self.operation[start_idx].isdigit():
                    self.make_parenthesis(start_idx, count)

        origin_post_op = self.change_post(self.operation)
        answer = self.do_operation(origin_post_op)
        for pos in self.paren_pos:
            new_op = self.insert_paren(pos)
            post_op = self.change_post(new_op)
            answer = max(answer, self.do_operation(post_op))

        print(answer)


if __name__ == '__main__':
    Main()