from sys import stdin


class Main:
    def __init__(self):
        self.num_of_people = 0
        self.num_of_party = 0
        self.knowing_people = None
        self.parent = None
        self.party = []

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
        self.num_of_people, self.num_of_party = map(int, stdin.readline().split())
        self.parent = [i for i in range(self.num_of_people + 1)]

        knowing_people_info = list(map(int, stdin.readline().split()))
        if knowing_people_info[0] != 0:
            self.knowing_people = set(knowing_people_info[1:])
        else:
            self.knowing_people = set()

        for _ in range(self.num_of_party):
            cur_num_of_people, *cur_people = list(map(int, stdin.readline().split()))

            self.party.append(cur_people)
            for person_1, person_2 in zip(cur_people, cur_people[1:]):
                if person_2 in self.knowing_people:
                    self.merge(person_2, person_1)
                else:
                    self.merge(person_1, person_2)

        num_of_party = 0
        for cur_party in self.party:
            for person in cur_party:
                person_parent = self.find(person)
                if person_parent in self.knowing_people:
                    break
            else:
                num_of_party += 1

        print(num_of_party)


if __name__ == '__main__':
    Main()