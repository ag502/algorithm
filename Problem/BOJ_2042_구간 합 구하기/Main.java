import java.util.*;
import java.io.*;

class Main {
    static int numOfNumbers, numOfUpdates, numOfSubSums;
    static long[] numbers;
    static long[] segTree;

    static StringTokenizer st;

    public static long initSegmentTree(int curNode, int start, int end) {
        if (start == end) {
            segTree[curNode] = numbers[start];
            return segTree[curNode];
        }
        int mid = (start + end) / 2;
        segTree[curNode] = initSegmentTree(curNode * 2, start, mid) + initSegmentTree((curNode * 2) + 1, mid + 1, end);
        return segTree[curNode];
    }

    public static void updateSegmentTree(int curNode, int start, int end, int updateIdx, long diff) {
        if (updateIdx < start || end < updateIdx) {
            return;
        }
        segTree[curNode] += diff;

        if (start == end) {
            return;
        }
        int mid = (start + end) / 2;
        updateSegmentTree(curNode * 2, start, mid, updateIdx, diff);
        updateSegmentTree((curNode * 2) + 1, mid + 1, end, updateIdx, diff);
    }

    public static long getSegmentTreeSum(int curNode, int start, int end, int left, int right) {
        // 범위 밖에 있는 경우
        if (right < start || end < left) {
            return 0;
        }

        // 범위 안에 있는 경우
        if (left <= start && end <= right) {
            return segTree[curNode];
        }

        int mid = (start + end) / 2;
        return getSegmentTreeSum(curNode * 2, start, mid, left, right)
                + getSegmentTreeSum((curNode * 2) + 1, mid + 1, end, left, right);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2042_구간 합 구하기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfNumbers = Integer.parseInt(st.nextToken());
        numOfUpdates = Integer.parseInt(st.nextToken());
        numOfSubSums = Integer.parseInt(st.nextToken());

        numbers = new long[numOfNumbers + 1];
        for (int idx = 1; idx <= numOfNumbers; idx++) {
            numbers[idx] = Integer.parseInt(br.readLine());
        }

        // 세그먼트 트리 초기화
        segTree = new long[numOfNumbers * 4];
        initSegmentTree(1, 1, numOfNumbers);

        // 수정, 합구하기
        for (int i = 0; i < numOfUpdates + numOfSubSums; i++) {
            st = new StringTokenizer(br.readLine());
            int command = Integer.parseInt(st.nextToken());

            if (command == 1) {
                int updateIdx = Integer.parseInt(st.nextToken());
                long updateNum = Long.parseLong(st.nextToken());

                updateSegmentTree(1, 1, numOfNumbers, updateIdx, updateNum - numbers[updateIdx]);
                numbers[updateIdx] = updateNum;
            } else if (command == 2) {
                int left = Integer.parseInt(st.nextToken());
                int right = Integer.parseInt(st.nextToken());

                long result = getSegmentTreeSum(1, 1, numOfNumbers, left, right);
                System.out.println(result);
            }
        }
    }
}