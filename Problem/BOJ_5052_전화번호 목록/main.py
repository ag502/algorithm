from sys import stdin


def main():
    stdin = open("./input.txt")
    test_case = int(stdin.readline())

    for _ in range(test_case):
        num_of_phone_number = int(stdin.readline())

        # 전화번호 목록 리스트
        phone_numbers = []
        for _ in range(num_of_phone_number):
            phone_numbers.append(stdin.readline().rstrip())

        # 길이 순 정렬
        phone_numbers.sort(key=lambda x: len(x))

        front_part_of_number = set()

        max_len = len(phone_numbers[0])
        front_part_of_number.add(phone_numbers[0])

        for phone_number in phone_numbers[1:]:
            for num_of_char in range(1, max_len + 1):
                if phone_number[:num_of_char] in front_part_of_number:
                    print("NO")
                    break
            else:
                # 전화번호 접두어 저장
                front_part_of_number.add(phone_number)
                max_len = len(phone_number)
                continue
            break
        else:
            print("YES")


if __name__ == '__main__':
    main()