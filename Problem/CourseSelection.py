def course_selection(course_list):
    course_list.sort(key=lambda element: element[1])
    selected_courses = []
    current_course = course_list[0]
    selected_courses.append(current_course)
    for i in range(1, len(course_list)):
        # start_time = course_list[i][0]
        # if (start_time < current_course[0]) | (start_time >= current_course[0]) & (start_time <= current_course[1]):
        #     continue
        # else:
        #     selected_courses.append(course_list[i])
        #     current_course = course_list[i]
        if current_course[1] <= course_list[i][0]:
            selected_courses.append(course_list[i])
            current_course = course_list[i]
    return selected_courses


print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
