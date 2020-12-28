from sys import stdin, maxsize


def main():
    stdin = open('./input.txt', 'r')
    num_of_lessons, num_of_blue_ray = map(int, stdin.readline().split())
    lessons = list(map(int, stdin.readline().split()))

    start = lessons[num_of_lessons - 1]
    end = maxsize

    while start <= end:
        mid = (start + end) // 2
        count = 0
        total_lessons_time = 0
        for idx in range(num_of_lessons - 1):
            total_lessons_time += lessons[idx]
            if total_lessons_time + lessons[idx + 1] > mid:
                total_lessons_time = 0
                count += 1
                print(mid, count)

        if total_lessons_time != 0:
            count += 1

        if count < num_of_blue_ray:
            end = mid - 1
        elif count > num_of_blue_ray:
            start = mid + 1
        else:
            print(mid)
            return

    print(start)


if __name__ == '__main__':
    main()