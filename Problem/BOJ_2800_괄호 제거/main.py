from sys import stdin
from collections import deque
from itertools import combinations

def process_exp(expression):
    parenthesis = deque()
    parenthesis_position = []
    num_of_char = 0
    original_exp = ''
    for char in expression:
        if char == '(':
            parenthesis.append([num_of_char, -1])
        elif char == ")":
            parenthesis_pair = parenthesis.pop()
            parenthesis_pair[1] = num_of_char
            parenthesis_position.append(parenthesis_pair)
        else:
            num_of_char += 1
        original_exp += char
    return parenthesis_position, original_exp

def main():
    math_exp = stdin.readline().rstrip()
    paren_position, original_exp = process_exp(math_exp)
    comb_paren = []
    case_of_expression = set()

    for i in range(1, len(paren_position)):
        comb_paren.append(list(combinations(paren_position, i)))
    case_of_expression.add(original_exp)

    print(paren_position)
    print(comb_paren)


if __name__ == '__main__':
    main()