from sys import stdin
from itertools import combinations

def main():
    stdin = open('./test_case.txt', 'r')
    num_of_players = int(stdin.readline())
    cards = []
    score = {}

    for _ in range(num_of_players):
        card = list(map(int, stdin.readline().split()))
        cards.append(card)

    for player, card in enumerate(cards):
        three_card_com = list(combinations(card, 3))
        max_sum = 0
        for com in three_card_com:
            max_sum = max(max_sum, sum(com) % 10)
        score[player + 1] = max_sum

    score = sorted(score.items(), key=lambda x: (-x[1], -x[0]))
    print(score[0][0])

if __name__ == '__main__':
    main()