import java.util.*;
import java.io.*;

public class Main {
    static int numOfLives, numOfQueries;
    static int[] prices;
    static long[] segTree;

    static StringTokenizer st;

    public static void update(int curNode, int index, int start, int end, int diff) {
        if (index < start || end < index) {
            return;
        }

        if (start <= index && index <= end) {
            segTree[curNode] += diff;
        }

        if (start == end) {
            return;
        }

        int mid = (start + end) / 2;
        update((curNode * 2), index, start, mid, diff);
        update((curNode * 2) + 1, index, mid + 1, end, diff);
    }

    public static long find(int curNode, int start, int end, int left, int right) {
        if (right < start || end < left) {
            return 0;
        }
        if (left <= start && end <= right) {
            return segTree[curNode];
        }

        int mid = (start + end) / 2;
        return find(curNode * 2, start, mid, left, right) + find((curNode * 2) + 1, mid + 1, end, left, right);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_12837_가계부 (Hard)\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfLives = Integer.parseInt(st.nextToken());
        numOfQueries = Integer.parseInt(st.nextToken());

        prices = new int[numOfLives + 1];
        segTree = new long[numOfLives * 4];

        for (int q = 1; q <= numOfQueries; q++) {
            st = new StringTokenizer(br.readLine());
            int queryType = Integer.parseInt(st.nextToken());

            if (queryType == 1) {
                int date = Integer.parseInt(st.nextToken());
                int price = Integer.parseInt(st.nextToken());
                update(1, date, 1, numOfLives, price);
                prices[date] = price;
            } else if (queryType == 2) {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());
                System.out.println(find(1, 1, numOfLives, left, right));
            }
        }
    }
}