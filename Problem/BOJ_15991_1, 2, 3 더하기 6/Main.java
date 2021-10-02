import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_15991_1, 2, 3 더하기 6\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        int testCase = Integer.parseInt(st.nextToken());

        // dp 초기화
        long[] dp = new long[100001];
        dp[0] = 1;
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 2;
        dp[4] = 3;

        for (int i = 5; i <= 100000; i++) {
            if (i - 2 >= 0) {
                dp[i] += dp[i - 2];
            }
            if (i - 4 >= 0) {
                dp[i] += dp[i - 4];
            }
            if (i - 6 >= 0) {
                dp[i] += dp[i - 6];
            }
            dp[i] = dp[i] % 1000000009;
        }

        // 테스트 케이스
        for (int t = 0; t < testCase; t++) {
            st = new StringTokenizer(br.readLine());
            System.out.println(dp[Integer.parseInt(st.nextToken())]);
        }
    }
}