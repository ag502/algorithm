from sys import stdin

def is_number(string):
    try:
        int(string)
        return True
    except:
        return False

def main():
    num_of_poketmon, num_of_problem = map(int, stdin.readline().split())
    poketmon_list = {}

    for i in range(num_of_poketmon):
        poketmon_name = stdin.readline().rstrip()
        poketmon_list[poketmon_name] = i

    poketmon_list_sort = sorted(poketmon_list.items(), key=lambda x: x[1])

    for _ in range(num_of_problem):
        problem = stdin.readline().rstrip()
        if is_number(problem):
            print(poketmon_list_sort[int(problem) - 1][0])
        else:
            print(poketmon_list[problem] + 1)

if __name__ == '__main__':
    main()