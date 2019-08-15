class DoublyLinkedList {
    int listSize = 0;
    Node head = null;
    Node tail = null;

    class Node {
        Node previous = null;
        Node next = null;
        int value = 0;

        private Node(Node previousNode, Node nextNode, int value) {
            this.previous = previousNode;
            this.next = nextNode;
            this.value = value;
        }

        private void setPreviousNode(Node previousNode) {
            this.previous = previousNode;
        }

        private void setNextNode(Node nextNode) {
            this.next = nextNode;
        }

        private Node getPreviousNode() {
            return this.previous;
        }

        private Node getNextNode() {
            return this.next;
        }

        private int getValue() {
            return value;
        }
    }

    public void addLast(int value) {
        if (listSize == 0) {
            addFirst(value);
        } else {
            Node newNode = new Node(tail, null, value);
            tail.setNextNode(newNode);
            tail = newNode;
            listSize++;
        }
    }

    public void addFirst(int value) {
        if (listSize == 0) {
            Node newNode = new Node(null, null, value);
            head = newNode;
            tail = newNode;
            listSize++;
        } else {
            Node newNode = new Node(null, head, value);
            head.setPreviousNode(newNode);
            head = newNode;
            listSize++;
        }
    }

    private Node getNodeFromFront(int index) {
        if (index > listSize) {
            return null;
        }

        Node node = head;

        for (int i = 0; i < index; i++) {
            node = node.getNextNode();
        }
        return node;
    }

    private Node getNodeFromEnd(int index) {
        if (index > listSize) {
            return null;
        }

        Node node = tail;

        for (int i = listSize - 1; i > index; i--) {
            node = node.getPreviousNode();
        }

        return node;
    }

    public Node getNode(int index) {
        if (index <= listSize / 2) {
            Node node = getNodeFromFront(index);
            return node;
        } else {
            Node node = getNodeFromEnd(index);
            return node;
        }
    }

    public static int getNodeValue(Node node) {
        return node.getValue();
    }

    public Node search(int value) {
        for (int i = 0; i < listSize; i++) {
            if (value == getNodeValue(getNode(i))) {
                return getNode(i);
            }
        }
        return null;
    }

    public void remove(Node node) {
        if (listSize == 1) {
            head = null;
            tail = null;
        } else {
            if (node == head) {
                head.getNextNode().setPreviousNode(null);
                head = head.getNextNode();
            } else if (node == tail) {
                tail.getPreviousNode().setNextNode(null);
                tail = tail.getPreviousNode();
            } else {
                node.getPreviousNode().setNextNode(node.getNextNode());
                node.getNextNode().setPreviousNode(node.getPreviousNode());
                node.setPreviousNode(null);
                node.setNextNode(null);
            }
        }
        listSize--;
    }

}

class Main {
    public static void main(String[] args) {
        DoublyLinkedList dbl = new DoublyLinkedList();
        dbl.addFirst(1);
        dbl.addFirst(2);
        dbl.addLast(3);
        dbl.addLast(5);
        dbl.addLast(7);
        dbl.addLast(9);

        for (int i = 0; i < dbl.listSize; i++) {
            System.out.println(DoublyLinkedList.getNodeValue(dbl.getNode(i)));
        }

        System.out.println("----------------------");

        dbl.remove(dbl.search(2));

        for (int i = 0; i < dbl.listSize; i++) {
            System.out.println(DoublyLinkedList.getNodeValue(dbl.getNode(i)));
        }
    }
}