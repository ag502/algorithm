from sys import stdin, maxsize


def calculate_relation_distance(mbti_1, mbti_2):
    relation_distance = 0
    for type_1, type_2 in zip(mbti_1, mbti_2):
        if type_1 != type_2:
            relation_distance += 1

    return relation_distance


def main():
    stdin = open('./input.txt', 'r')
    test_case = int(stdin.readline())
    for _ in range(test_case):
        num_of_students = int(stdin.readline())
        mbti = list(stdin.readline().split())

        if num_of_students >= 33:
            print(0)
            continue

        relation_distance = maxsize
        for i in range(num_of_students - 2):
            for j in range(i + 1, num_of_students - 1):
                for k in range(j + 1, num_of_students):
                    relation_distance = min(relation_distance,
                                            calculate_relation_distance(mbti[i], mbti[j]) +
                                            calculate_relation_distance(mbti[j], mbti[k]) +
                                            calculate_relation_distance(mbti[i], mbti[k])
                                            )

        print(relation_distance)


if __name__ == '__main__':
    main()