from sys import stdin, maxsize


class Main:
    def __init__(self):
        self.num_of_ingredient = 0
        self.taste_score = []
        self.selected_ingredients = []
        self.taste_diff = maxsize

        self.main()

    def select_ingredient(self, cur_ingredient, kinds, cur_ingredients=[]):
        cur_ingredients.append(cur_ingredient)

        if len(cur_ingredients) < kinds:
            for next_ingredient in range(cur_ingredient + 1, self.num_of_ingredient):
                self.select_ingredient(next_ingredient, kinds, cur_ingredients)

        elif len(cur_ingredients) == kinds:
            self.selected_ingredients.append(cur_ingredients[:])
        cur_ingredients.pop()

    def calc_taste(self, ingredients):
        sour_score = 1
        bitter_score = 0
        for ingredient in ingredients:
            sour, bitter = self.taste_score[ingredient]
            sour_score *= sour
            bitter_score += bitter
        return sour_score, bitter_score

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_ingredient = int(stdin.readline())

        for _ in range(self.num_of_ingredient):
            self.taste_score.append(list(map(int, stdin.readline().split())))

        for i in range(1, self.num_of_ingredient + 1):
            for start_ingredient in range(self.num_of_ingredient):
                self.select_ingredient(start_ingredient, i)

        for ingredients in self.selected_ingredients:
            sour_score, bitter_score = self.calc_taste(ingredients)
            self.taste_diff = min(self.taste_diff, abs(sour_score - bitter_score))

        print(self.taste_diff)


if __name__ == '__main__':
    Main()