from sys import stdin

def time_parsing(time):
    hour, minute = list(map(int, time.split(":")))

    converted_hour = hour
    if hour > 12:
        converted_hour = hour - 12

    if minute == 0:
        converted_minute = 12
    else:
        converted_minute = round(minute / 5, 2)

    degree = abs(converted_hour - converted_minute)
    if degree > 6:
        degree = 12 - degree
    return hour, degree

def main():
    test_case = int(stdin.readline())
    time_list = [stdin.readline().split() for _ in range(test_case)]

    sorted_degree = []
    for case in time_list:
        temp = []
        for time in case:
            hour, degree = time_parsing(time)
            temp.append((time, hour, degree))
        temp.sort(key=lambda x: (x[2], x[1]))
        sorted_degree.append(temp)

    # for case in sorted_degree:
    #     print(case[2][0])
    print(sorted_degree)

if __name__ == "__main__":
    main()