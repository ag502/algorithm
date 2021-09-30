import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14501_퇴사\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        int days = Integer.parseInt(st.nextToken());
        int[] times = new int[days + 1];
        int[] prices = new int[days + 1];

        for (int i = 1; i <= days; i++) {
            st = new StringTokenizer(br.readLine());
            times[i] = Integer.parseInt(st.nextToken());
            prices[i] = Integer.parseInt(st.nextToken());
        }

        // dp
        int[] dp = new int[days + 1];
        if (times[1] <= days) {
            dp[1] = prices[1];
        }

        for (int day = 2; day <= days; day++) {
            if (times[day] + day - 1 <= days) {
                dp[day] = prices[day];
            }
            for (int prevDay = 1; prevDay < day; prevDay++) {
                if (day > prevDay + times[prevDay] - 1 && times[day] + day - 1 <= days) {
                    dp[day] = Math.max(dp[day], dp[prevDay] + prices[day]);
                }
            }
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}