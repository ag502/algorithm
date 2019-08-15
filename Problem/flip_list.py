class FlipList:
    def flip(self, some_list):
        if len(some_list) == 1:
            return some_list
        # return self.flip(some_list[(len(some_list) // 2):]) + self.flip(some_list[:len(some_list) // 2])
        return some_list[-1:] + self.flip(some_list[0:-1])


some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(FlipList().flip(some_list))
