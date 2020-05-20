from sys import stdin

def main():
    frame_number = int(stdin.readline())
    total_recommend = int(stdin.readline())
    recommend_list = list(map(int, stdin.readline().split()))

    frame = {}

    for student in recommend_list:
        if student in frame:
            frame[student] += 1
        else:
            if len(frame) < frame_number:
                frame[student] = 1
            else:
                sorted_frame = sorted(frame.items(), key=lambda x: x[1])
                del frame[sorted_frame[0][0]]
                frame[student] = 1
    final_student = sorted(frame.items(), key=lambda x: x[0])

    result = ''
    for student, number in final_student:
        result += str(student) + ' '
    print(result.strip())

if __name__ == "__main__":
    main()