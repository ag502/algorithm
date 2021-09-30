import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\grm_10C\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 입력받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        int numOfClasses = Integer.parseInt(st.nextToken());

        int[] insentives = new int[numOfClasses];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < numOfClasses; i++) {
            insentives[i] = Integer.parseInt(st.nextToken());
        }

        // dp 배열
        int[][] dp = new int[3][numOfClasses];

        dp[1][0] = insentives[0];

        for (int i = 1; i < numOfClasses; i++) {
            // 연속 1일
            if (i == 1) {
                dp[1][i] = insentives[i];
            } else {
                dp[1][i] = Math.max(insentives[i], dp[2][i - 2] + insentives[i]);
            }

            // 연속 2일
            if (i == 1) {
                dp[2][i] = insentives[i] + dp[1][i - 1];
            } else {
                dp[2][i] = dp[1][i - 1] + insentives[i];
            }
        }

        int answer = Integer.MIN_VALUE;
        for (int row = 1; row < 3; row++) {
            for (int col = 0; col < numOfClasses; col++) {
                answer = Math.max(answer, dp[row][col]);
            }
        }
        System.out.println(answer);
    }
}