import java.util.*;
import java.io.*;

class Main {
    static int numOfA, numOfB;
    static int[] a, b;

    static StringTokenizer st;

    // 찾고자 하는 값 미만 인 값들 중 가장 큰 값 찾기
    public static int binarySearch(int targetValue) {
        int leftIdx = 0;
        int rightIdx = b.length - 1;

        int result = -1;
        while (leftIdx <= rightIdx) {
            int midIdx = (leftIdx + rightIdx) / 2;
            if (b[midIdx] < targetValue) {
                result = midIdx;
                leftIdx = midIdx + 1;
            } else {
                rightIdx = midIdx - 1;
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_7795_먹을 것인가 먹힐 것인가\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        int testCase = Integer.parseInt(br.readLine());
        for (int test = 0; test < testCase; test++) {

            // 테스트 케이스 입력
            st = new StringTokenizer(br.readLine());
            numOfA = Integer.parseInt(st.nextToken());
            numOfB = Integer.parseInt(st.nextToken());

            a = new int[numOfA];
            b = new int[numOfB];

            // a, b 크기 입력
            st = new StringTokenizer(br.readLine());
            for (int idx = 0; idx < numOfA; idx++) {
                a[idx] = Integer.parseInt(st.nextToken());
            }

            st = new StringTokenizer(br.readLine());
            for (int idx = 0; idx < numOfB; idx++) {
                b[idx] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(b);

            // a 보다 크기가 큰 b 찾기
            int answer = 0;
            for (int idx = 0; idx < numOfA; idx++) {
                int findIdx = binarySearch(a[idx]);
                if (findIdx != -1) {
                    answer += findIdx + 1;
                }
            }

            System.out.println(answer);
        }
    }
}