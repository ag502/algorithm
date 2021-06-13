from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 5)


class Main:
    def __init__(self):
        self.num_of_neuron = None
        self.num_of_synapse = None
        self.parent = None

        self.main()

    def find_parent(self, neuron):
        if self.parent[neuron] == neuron:
            return neuron
        self.parent[neuron] = self.find_parent(self.parent[neuron])
        return self.parent[neuron]

    def merge(self, neuron_1, neuron_2):
        neuron_1_parent = self.find_parent(neuron_1)
        neuron_2_parent = self.find_parent(neuron_2)

        if neuron_1_parent == neuron_2_parent:
            return True
        self.parent[neuron_2_parent] = neuron_1_parent
        return False

    def main(self):
        stdin = open("./input.txt", "r")
        self.num_of_neuron, self.num_of_synapse = map(int, stdin.readline().split())
        self.parent = [i for i in range(self.num_of_neuron + 1)]

        num_of_cycle = 0
        for _ in range(self.num_of_synapse):
            neuron_1, neuron_2 = map(int, stdin.readline().split())
            neuron_1_parent = self.find_parent(neuron_1)
            neuron_2_parent = self.find_parent(neuron_2)

            is_cycle = self.merge(neuron_1_parent, neuron_2_parent)
            if is_cycle:
                num_of_cycle += 1

        parent_list = set()
        for neuron in range(1, self.num_of_neuron + 1):
            parent = self.find_parent(neuron)
            parent_list.add(parent)

        print(len(parent_list) - 1 + num_of_cycle)


if __name__ == '__main__':
    Main()