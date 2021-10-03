import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_2579_계단 오르기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numOfStairs = Integer.parseInt(st.nextToken());
        int[] stairs = new int[numOfStairs + 1];

        for (int stair = 1; stair <= numOfStairs; stair++) {
            stairs[stair] = Integer.parseInt(br.readLine());
        }

        // dp
        int[][] dp = new int[3][numOfStairs + 1];
        dp[1][1] = stairs[1];
        dp[2][1] = 0;

        if (numOfStairs >= 2) {
            dp[1][2] = stairs[2];
            dp[2][2] = dp[1][1] + stairs[2];
        }

        for (int stair = 3; stair <= numOfStairs; stair++) {
            dp[1][stair] = Math.max(dp[1][stair - 2], dp[2][stair - 2]) + stairs[stair];
            dp[2][stair] = dp[1][stair - 1] + stairs[stair];
        }

        System.out.println(Math.max(dp[1][numOfStairs], dp[2][numOfStairs]));
    }
}