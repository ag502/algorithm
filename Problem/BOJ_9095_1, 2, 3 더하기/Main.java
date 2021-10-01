import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_9095_1, 2, 3 더하기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        int testCase = Integer.parseInt(st.nextToken());

        // dp 초기화
        int[] dp = new int[11];

        // 초기값
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;

        // 점화식
        for (int i = 4; i <= 10; i++) {
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3];
        }


        for (int t = 0; t < testCase; t++) {
            st = new StringTokenizer(br.readLine());
            System.out.println(dp[Integer.parseInt(st.nextToken())]);
        }
    }
}