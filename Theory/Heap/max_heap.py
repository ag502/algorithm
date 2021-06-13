class MaxHeap:
    def __init__(self):
        self.heap = [None]

    def insert(self, value):
        self.heap.append(value)
        cur_idx = len(self.heap) - 1

        while cur_idx != 1:
            parent = cur_idx // 2

            if self.heap[cur_idx] > self.heap[parent]:
                self.heap[cur_idx], self.heap[parent] = [self.heap[parent], self.heap[cur_idx]]
                cur_idx = parent
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
            elif left_child != -1 and right_child == -1:
                child = left_child
            else:
                child = left_child if self.heap[left_child] > self.heap[right_child] else right_child

            if child == -1:
                break

            if self.heap[cur_idx] < self.heap[child]:
                self.heap[cur_idx], self.heap[child] = [self.heap[child], self.heap[cur_idx]]
                cur_idx = child
            else:
                break


if __name__ == "__main__":
    max_heap = MaxHeap()

    max_heap.insert(5)
    max_heap.insert(10)
    max_heap.insert(11)
    max_heap.insert(3)
    max_heap.insert(5)
    max_heap.insert(111)
    max_heap.insert(8)

    max_heap.remove()
    max_heap.remove()
    max_heap.remove()
    max_heap.remove()

    max_heap.insert(4)
    max_heap.insert(7)

    max_heap.remove()
    max_heap.remove()
    max_heap.remove()
    max_heap.remove()
    max_heap.remove()

    print(max_heap.heap)