import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_11052_카드 구매하기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());

        int numOfCards = Integer.parseInt(st.nextToken());
        int[] prices = new int[numOfCards + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= numOfCards; i++) {
            prices[i] = Integer.parseInt(st.nextToken());
        }

        // dp 초기화
        int[] dp = new int[numOfCards + 1];
        for (int i = 1; i < numOfCards + 1; i++) {
            for (int j = 1; j <= i; j++) {
                dp[i] = Math.max(dp[i], dp[i - j] + prices[j]);
            }
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}