class BinarySearch:
    def binary_search(self, element, some_list, start_index=0, end_index=None):
        if end_index == None:
            end_index = len(some_list) - 1

        self.mid_index = (start_index + end_index) // 2

        if start_index > end_index:
            return None

        if some_list[self.mid_index] == element:
            return self.mid_index
        elif some_list[self.mid_index] < element:
            return self.binary_search(element, some_list, self.mid_index + 1, end_index)
        elif some_list[self.mid_index] > element:
            return self.binary_search(element, some_list, start_index, self.mid_index - 1)


print(BinarySearch().binary_search(2, [2, 3, 5, 7, 11]))
print(BinarySearch().binary_search(0, [2, 3, 5, 7, 11]))
print(BinarySearch().binary_search(5, [2, 3, 5, 7, 11]))
print(BinarySearch().binary_search(3, [2, 3, 5, 7, 11]))
print(BinarySearch().binary_search(11, [2, 3, 5, 7, 11]))
