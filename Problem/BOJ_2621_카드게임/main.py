from sys import stdin

def main():
    cards = []
    for _ in range(5):
        card = stdin.readline().split()
        cards.append(card)
    cards = sorted(cards, key=lambda x: x[1])
    info = verify_cards(cards)

    answer = 0
    if info['all_same_color'] and info['all_continuous']:
        answer = info['max_num'] + 900
    elif info['four_same_number'] != False:
        answer = info['four_same_number'][1] + 800
    elif info['three_same_number'] != False and info['two_same_number_1'] != False:
        answer = info['three_same_number'][1] * 10 + info['two_same_number_1'][1] + 700
    elif info['all_same_color']:
        answer = info['max_num'] + 600
    elif info['all_continuous']:
        answer = info['max_num'] + 500
    elif info['three_same_number'] != False:
        answer = info['three_same_number'][1] + 400
    elif info['two_same_number_1'] != False and info['two_same_number_2'] != False:
        answer = max(info['two_same_number_1'][1], info['two_same_number_2'][1]) * 10 + \
            min(info['two_same_number_1'][1], info['two_same_number_2'][1]) + 300
    elif info['two_same_number_1'] != False and not info['two_same_number_2']:
        answer = info['two_same_number_1'][1] + 200
    else:
        answer = info['max_num'] + 100
    print(answer)

def verify_cards(cards):
    info = {
        'all_same_color': False,
        'all_continuous': False,
        'two_same_number_1': False,
        'two_same_number_2' : False,
        'three_same_number': False,
        'four_same_number': False,
        'max_num': int(cards[4][1])
    }
    cards_number = {}
    cards_color = set()

    prev_num = 0
    cur_num = 0
    flag = False
    for idx, card in enumerate(cards):
        color = card[0]
        number = int(card[1])
        cur_num = number

        cards_color.add(color)
        if number in cards_number:
            cards_number[number] += 1
        else:
            cards_number[number] = 1

        if idx != 0:
            if cur_num - prev_num == 1 and not flag:
                info['all_continuous'] = True
            else:
                flag = True
                info['all_continuous'] = False
        prev_num = cur_num

    if len(cards_color) == 1:
        info['all_same_color'] = True

    for number, num_count in cards_number.items():
        if num_count == 4:
            info['four_same_number'] = [True, number]
        elif num_count == 3:
            info['three_same_number'] = [True, number]
        elif num_count == 2:
            if not info['two_same_number_1']:
                info['two_same_number_1'] = [True, number]
            else:
                info['two_same_number_2'] = [True, number]

    return info

if __name__ == '__main__':
    main()