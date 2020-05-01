from sys import stdin

def time_parsing(time):
    hour, minute = list(map(int, time.split(":")))

    converted_hour = hour
    if hour >= 12:
        converted_hour = hour - 12

    degree = abs(converted_hour * 30 - minute * 5.5)
    if degree > 180:
        degree = 360 - degree
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

    for case in sorted_degree:
        print(case[2][0])
    # print(sorted_degree)

if __name__ == "__main__":
    main()