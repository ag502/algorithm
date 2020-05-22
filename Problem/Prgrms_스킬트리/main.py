from sys import stdin

def main():
    pre_skill_list = list(stdin.readline().rstrip())
    skill_trees = list(stdin.readline().split())
    answer = 0

    for skill_list in skill_trees:
        is_possible = True
        copy_pre_skill = pre_skill_list.copy()
        one_skill_list = list(skill_list)
        for skill in one_skill_list:
            if skill in pre_skill_list:
                margin = pre_skill_list.index(skill)
                copy_pre_skill[margin] = -1
                for index in range(0, margin):
                    if copy_pre_skill[index] != -1:
                        is_possible = False
                        break
            if not is_possible:
                break
        if is_possible:
            answer += 1

    print(answer)

if __name__ == "__main__":
    main()