class MinHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self, value):
        self.heap.append(value)
        cur_idx = len(self.heap) - 1

        while cur_idx != 1:
            parent_idx = cur_idx // 2

            if self.heap[cur_idx] < self.heap[parent_idx]:
                self.heap[cur_idx], self.heap[parent_idx] = [self.heap[parent_idx], self.heap[cur_idx]]
                cur_idx = parent_idx
            else:
                break

    def remove(self):
        if len(self.heap) == 1:
            return
        print(self.heap[1])
        self.heap[1] = self.heap[len(self.heap) - 1]
        self.heap.pop()

        cur_idx = 1
        while True:
            left_child = -1 if cur_idx * 2 >= len(self.heap) else cur_idx * 2
            right_child = -1 if (cur_idx * 2) + 1 >= len(self.heap) else (cur_idx * 2) + 1

            if left_child == -1 and right_child == -1:
                child = -1
            elif left_child != - 1 and right_child == -1:
                child = -1
            else:
                child = left_child if self.heap[left_child] < self.heap[right_child] else right_child

            if child == -1:
                break

            if self.heap[child] < self.heap[cur_idx]:
                self.heap[cur_idx], self.heap[child] = [self.heap[child], self.heap[cur_idx]]
                cur_idx = child
            else:
                break


if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.insert(3)
    min_heap.insert(10)
    min_heap.insert(35)
    min_heap.insert(23)
    min_heap.insert(19)
    min_heap.insert(47)
    min_heap.insert(60)
    min_heap.insert(35)
    min_heap.insert(80)
    min_heap.insert(44)
    min_heap.insert(5)

    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()
    min_heap.remove()

    print(min_heap.heap)