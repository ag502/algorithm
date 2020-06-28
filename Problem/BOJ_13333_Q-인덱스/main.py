from sys import stdin

def find_q_index(index, paper_list):
    num_of_below, num_of_above, num_of_same = 0, 0, 0
    num_of_paper = len(paper_list)

    for reference_time in paper_list:
        if reference_time >= index:
            num_of_above += 1
            if reference_time == index:
                num_of_same += 1
        else:
            num_of_below += 1

    if num_of_above >= index:
        if num_of_below == num_of_paper - index:
            return True
        else:
            while num_of_same != 0:
                num_of_above -= 1
                num_of_below += 1
                num_of_same -= 1

                if num_of_above < index:
                    return False
                else:
                    if num_of_below == num_of_paper - index:
                        return True
    return False


def main():
    n = int(stdin.readline())
    paper_list = list(map(int, stdin.readline().split()))

    end_index = max(paper_list)

    for index in range(0, end_index + 1):
        if find_q_index(index, paper_list):
            print(index)
            return

if __name__ == '__main__':
    main()
