from sys import stdin

def has_car(car_name, rent_info):
    for index, info in enumerate(rent_info):
        name, distance, add_cost = info
        if car_name == name:
            return index
    return -1

def main():
    test_case = int(stdin.readline())
    num_of_car, num_of_event = map(int, stdin.readline().split())
    car_list, spy_status, spy_info = {}, {}, {}

    for _ in range(num_of_car):
        car_info = list(stdin.readline().split())
        car_list[car_info[0]] = car_info[1:]

    for _ in range(num_of_event):
        time, name, event_type, add_info = list(stdin.readline().split())
        if name not in spy_status:
            spy_status[name] = ''
            spy_info[name] = []
        if event_type == 'p':
            if spy_status[name] == '':
                spy_status[name] = 'p'
                spy_info[name].append([add_info, 0, 0])
            elif spy_status[name] == 'r':
                spy_status[name] = 'p'
                if has_car(add_info, spy_info[name]) == -1:
                    spy_info[name].append([add_info, 0, 0])

        elif event_type == 'a':
            if spy_status[name] == 'p':
                spy_status[name] = 'a'
                for 