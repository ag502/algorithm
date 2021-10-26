import java.util.*;
import java.io.*;

public class Main {
    static int numOfNumbers, numOfRanges;
    static int[] numbers;
    static int[] segTree;

    static StringTokenizer st;

    public static int initSeg(int curNode, int start, int end) {
        if (start == end) {
            segTree[curNode] = numbers[start];
            return segTree[curNode];
        }

        int mid = (start + end) / 2;
        segTree[curNode] = Math.min(initSeg(curNode * 2, start, mid), initSeg((curNode * 2) + 1, mid + 1, end));
        return segTree[curNode];
    }

    public static int find(int curNode, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return Integer.MAX_VALUE;
        }
        if (left <= start && end <= right) {
            return segTree[curNode];
        }
        int mid = (start + end) / 2;
        return Math.min(find(curNode * 2, start, mid, left, right),
                find(((curNode * 2) + 1), mid + 1, end, left, right));
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_10868_최솟값\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfNumbers = Integer.parseInt(st.nextToken());
        numOfRanges = Integer.parseInt(st.nextToken());

        numbers = new int[numOfNumbers + 1];
        for (int idx = 1; idx <= numOfNumbers; idx++) {
            numbers[idx] = Integer.parseInt(br.readLine());
        }

        segTree = new int[numOfNumbers * 4];
        initSeg(1, 1, numOfNumbers);

        for (int idx = 0; idx < numOfRanges; idx++) {
            st = new StringTokenizer(br.readLine());
            int left = Integer.parseInt(st.nextToken());
            int right = Integer.parseInt(st.nextToken());

            System.out.println(find(1, 1, numOfNumbers, left, right));
        }
    }
}
