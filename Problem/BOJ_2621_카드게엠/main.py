from sys import stdin

def identify_card(card_nums):
    # 1. 연속된 숫자
    is_continuous = True
    for idx in range(len(card_nums) - 1):
        if int(card_nums[idx + 1][0]) - int(card_nums[idx][0]) != 1:
            is_continuous = False
    if is_continuous:
        return 'CONTINUOUS'

    # 2. 4장이 같은 숫자
    is_four_same = False
    for number, count in card_nums:
        if count == 4:
            is_four_same = True
            break
    if is_four_same:
        return 'FOUR_SAME'

    # 3. 3장, 2장이 같음
    is_three_two_same = 0
    for number, count
def main():
    info = {'color': set(),
            'number': {},
            'max_num': 0,
            'min_num': 10,
            }

    for _ in range(5):
        color, number = list(stdin.readline().split())
        info['color'].add(color)

        if int(number) in info['number']:
            info['number'][number] += 1
        else:
            info['number'][number] = 1

        if int(number) > info['max_num']:
            info['max_num'] = int(number)
        if int(number) < info['min_num']:
            info['min_num'] = int(number)

    color_count = info['color']
    number_count = sorted(info['number'].items())
    answer = 0

    if len(color_count) == 1:
        is_continuous = True
        for idx in range(len(number_count) - 1):
            if int(number_count[idx + 1][0]) - int(number_count[idx][0]) != 1:
                is_continuous = False
                break
        if is_continuous:
            answer = info['max_num'] + 900
    # elif

    print(color_count)
    print(number_count)

if __name__ == '__main__':
    main()