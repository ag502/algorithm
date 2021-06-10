from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)


class Main:
    def __init__(self):
        self.num_of_people = None
        self.num_of_relation = None
        self.enemy = None
        self.parent = None

        self.main()

    def find(self, person):
        if self.parent[person] == person:
            return person
        self.parent[person] = self.find(self.parent[person])
        return self.parent[person]

    def merge(self, person_1, person_2):
        person_1_parent = self.find(person_1)
        person_2_parent = self.find(person_2)

        if person_1_parent == person_2_parent:
            return
        self.parent[person_2_parent] = person_1_parent

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_people, self.num_of_relation = map(int, stdin.readline().split())
        self.enemy = [i for i in range(0, self.num_of_people + 1)]
        self.parent = [i for i in range(0, self.num_of_people + 1)]

        # print(self.parent)

        for _ in range(self.num_of_relation):
            person_1, person_2 = map(int, stdin.readline().split())

            person_1_parent = self.find(person_1)
            person_2_parent = self.find(person_2)

            if person_1_parent == person_2_parent:
                print(0)
                return

            person_1_enemy = self.enemy[person_1]
            if person_1_enemy == person_1:
                self.enemy[person_1] = person_2
            else:
                self.merge(person_2, person_1_enemy)

            person_2_enemy = self.enemy[person_2]
            if person_2_enemy == person_2:
                self.enemy[person_2] = person_1
            else:
                self.merge(person_1, person_2_enemy)

        print(1)


if __name__ == '__main__':
    Main()