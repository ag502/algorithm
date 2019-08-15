class Node:
    def __init__(self, data, nextNode, prevNode):
        self.data = data
        self.nexNode = nextNode
        self.prevNode = prevNode

class DoublyLinkedList:
    def __init__(self):
        self.listSize = 0
        self.head = None
        self.tail = None
        
    def addFirst(self, data):
        if (self.listSize == 0):
            node = Node(data, None, None)
            self.head = node
            self.tail = node
        else:
            node = Node(data, self.head, None)
            self.head.prevNode = node
            self.head = node
        self.listSize += 1
        
    def addLast(self, data):
        if (self.listSize == 0):
            self.addFirst(data)
        else:
            node = Node(data, None, self.tail)
            self.tail.nexNode = node
            self.tail = node
            self.listSize += 1
        
    def getNodeFromFront(self, idx):
        node = self.head
        for i in range(0, idx):
            node = node.nexNode
        return node.data
    
    def getNodeFromEnd(self, idx):
        node = self.tail
        for i in range(self.listSize - 1, idx, -1):
            node = node.prevNode
        return node.data

    def getNode(self, node):
        return node.data
        
    def search(self, value):
        node = self.head
        for i in range(0, self.listSize):
            if (node.data == value):
                return node
            node = node.nexNode
        return node
        
    def remove(self, node):
        if (self.listSize == 1):
            self.head == None;
            self.tail == None;
        else:
            if (node == self.head):
                self.head = self.head.nexNode
                self.head.prevNode = None
            elif (node == self.tail):
                self.tail = self.tail.prevNode
                self.tail.nexNode = None
            else:
                node.prevNode.nexNode = node.nexNode
                node.nexNode.prevNode = node.prevNode
                node.prevNode = None
                node.nexNode = None
        self.listSize -= 1       
dbl = DoublyLinkedList();
dbl.addFirst(1)
dbl.addFirst(2)
dbl.addLast(5)
dbl.addLast(7)
dbl.addLast(8)

for i in range(0, dbl.listSize):
    print(dbl.getNodeFromEnd(i))

print("=============")

dbl.remove(dbl.search(5))


for i in range(0, dbl.listSize):
    print(dbl.getNodeFromEnd(i))
