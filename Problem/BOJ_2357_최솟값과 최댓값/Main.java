import java.util.*;
import java.io.*;

class Node {
    int min;
    int max;

    public Node(int min, int max) {
        this.min = min;
        this.max = max;
    }

    @Override
    public String toString() {
        return this.min + " " + this.max;
    }
}

public class Main {
    static int numOfNumbers, numOfRanges;
    static int[] numbers;
    static Node[] segTree;

    static StringTokenizer st;

    public static Node initSegment(int curNode, int start, int end) {
        if (start == end) {
            segTree[curNode] = new Node(numbers[start], numbers[end]);
            return segTree[curNode];
        }
        int mid = (start + end) / 2;
        Node left = initSegment(curNode * 2, start, mid);
        Node right = initSegment((curNode * 2) + 1, mid + 1, end);

        segTree[curNode] = new Node(Math.min(left.min, right.min), Math.max(left.max, right.max));
        return segTree[curNode];
    }

    public static Node getMinMaxValue(int curNode, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return new Node(Integer.MAX_VALUE, Integer.MIN_VALUE);
        }
        if (left <= start && end <= right) {
            return segTree[curNode];
        }
        int mid = (start + end) / 2;
        Node leftNode = getMinMaxValue(curNode * 2, start, mid, left, right);
        Node rightNode = getMinMaxValue((curNode * 2) + 1, mid + 1, end, left, right);

        return new Node(Math.min(leftNode.min, rightNode.min), Math.max(leftNode.max, rightNode.max));
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2357_최솟값과 최댓값\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfNumbers = Integer.parseInt(st.nextToken());
        numOfRanges = Integer.parseInt(st.nextToken());

        numbers = new int[numOfNumbers + 1];
        for (int i = 1; i <= numOfNumbers; i++) {
            numbers[i] = Integer.parseInt(br.readLine());
        }

        // 세그먼트 트리 초기화
        segTree = new Node[numOfNumbers * 4 + 1];
        initSegment(1, 1, numOfNumbers);

        for (int i = 0; i < numOfRanges; i++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            Node answer = getMinMaxValue(1, 1, numOfNumbers, left, right);
            System.out.println(answer);
        }
    }
}