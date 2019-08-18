class MaxProduct:
    def max_product(self, left_cards, right_cards):
        self.max = 0
        for i in left_cards:
            for j in right_cards:
                if self.max < i * j:
                    self.max = i * j
        return self.max


print(MaxProduct().max_product([1, 6, 5], [4, 2, 3]))
print(MaxProduct().max_product([1, -9, 3, 4], [2, 8, 3, 1]))
print(MaxProduct().max_product([-1, -7, 3], [-4, 3, 6]))
