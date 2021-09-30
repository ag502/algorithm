import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2011_암호코드\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 비밀번호 입력받기
        String password = br.readLine();
        int[] passwordAsInt = new int[password.length()];
        for (int i = 0; i < password.length(); i++) {
            passwordAsInt[i] = password.charAt(i) - '0';
        }

        // dp 배열
        int[] dp = new int[password.length()];
        if (passwordAsInt[0] == 0) {
            System.out.println(0);
            return;
        } else {
            dp[0] = 1;
        }

        for (int i = 1; i < passwordAsInt.length; i++) {
            // 한 글자 확인
            if (passwordAsInt[i] != 0) {
                dp[i] = (dp[i] + dp[i - 1]) % 1000000;
            }

            if (passwordAsInt[i - 1] != 0 && (passwordAsInt[i - 1] * 10 + passwordAsInt[i] <= 26)) {
                if (i == 1) {
                    dp[i] = (dp[i] + 1) % 1000000;
                } else {
                    dp[i] = (dp[i] + dp[i - 2]) % 1000000;
                }
            }

            if (dp[i] == 0) {
                System.out.println(0);
                return;
            }
        }

        // System.out.println(Arrays.toString(dp));
        System.out.println(dp[password.length() - 1]);
    }
}