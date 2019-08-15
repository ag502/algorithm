class Node {
    Node next;
    int data;

    public Node(Node nextNode, int value) {
        this.next = nextNode;
        this.data = value;
    }
}

class LinearLinkedList {
    int listSize;
    Node head;
    Node tail;

    public LinearLinkedList() {
        listSize = 0;
        head = null;
        tail = null;
    }

    public void addFirst(int value) {
        if (head == null) {
            Node node = new Node(null, value);
            head = node;
            tail = node;
        } else {
            Node node = new Node(head, value);
            head = node;
        }
        listSize++;
    }

    public void addLast(int value) {
        if (head == null) {
            addFirst(value);
        } else {
            Node node = new Node(null, value);
            tail.next = node;
            tail = node;
        }
        listSize++;
    }

    public void remove(int index) {
        if (listSize == 1) {
            head = null;
            tail = null;
        } else if (index == 0) {
            head = head.next;
        } else if (index == listSize - 1) {
            Node node = getNode(index - 1);
            node.next = null;
            tail = node;
        } else {
            Node curNode = getNode(index);
            Node preCurNode = getNode(index - 1);
            preCurNode.next = curNode.next;
            curNode = null;
        }
        listSize--;
    }

    public int search(int value) {
        if (listSize > 0) {
            Node node = head;
            for (int i = 0; i < listSize; i++) {
                if (node.data == value) {
                    return i;
                }
                node = node.next;
            }
            return -1;
        }
        return -1;
    }

    public Node getNode(int index) {
        if (index < listSize && index >= 0) {
            Node node = head;
            for (int i = 0; i < index; i++) {
                node = node.next;
            }
            return node;
        }
        return null;
    }

    public void printAllNodeValue() {
        if (listSize > 0) {
            Node node = head;
            for (int i = 0; i < listSize; i++) {
                System.out.print(node.data + " ");
                node = node.next;
            }
        }
    }
}

class Main {
    public static void main(String[] args) {
        LinearLinkedList linkedList = new LinearLinkedList();
        linkedList.addFirst(1);
        linkedList.addFirst(2);
        linkedList.addLast(3);
        linkedList.addLast(5);
        linkedList.addLast(8);
        linkedList.addLast(9);

        linkedList.printAllNodeValue();

        System.out.println();

        linkedList.remove(5);

        linkedList.printAllNodeValue();
    }
}