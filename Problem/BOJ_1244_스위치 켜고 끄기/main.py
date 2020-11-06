from sys import stdin

def on_off_light(cur_status):
    next_status = -1
    if cur_status == 1:
        next_status = 0
    elif cur_status == 0:
        next_status = 1
    return next_status

def change_status(lights, gender, light_num):
    # 남학생
    if gender == 1:
        for cur_light_num in range(light_num, len(lights), light_num):
            lights[cur_light_num] = on_off_light(lights[cur_light_num])
    # 여학생
    elif gender == 2:
        lights[light_num] = on_off_light(lights[light_num])

        count = 1
        while True:
            left_side = light_num - count
            right_side = light_num + count
            # 배열 범위 초과 (전구는 1번 부터 시작!!)
            if left_side <= 0 or right_side >= len(lights):
                break
            # 대칭이 아닐 경우
            if lights[left_side] != lights[right_side]:
                break
            else:
                lights[left_side] = on_off_light(lights[left_side])
                lights[right_side] = on_off_light(lights[right_side])
                count += 1


def main():
    stdin = open('./test_case.txt', 'r')
    num_of_lights = int(stdin.readline())
    lights = [0] + list(map(int, stdin.readline().split()))
    num_of_students = int(stdin.readline())

    for _ in range(num_of_students):
        gender, light_num = map(int, stdin.readline().split())
        change_status(lights, gender, light_num)

    answer = []
    for idx, light in enumerate(lights[1:]):
        answer.append(str(light))
        if len(answer) != 0 and len(answer) % 20 == 0:
            print(' '.join(answer))
            answer = []
    if len(answer) != 0:
        print(' '.join(answer))

if __name__ == '__main__':
    main()


