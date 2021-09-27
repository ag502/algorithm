import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    static int lenOfArray;
    static List<Integer> array;
    static int[] dp;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_13398_연속합 2\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        lenOfArray = Integer.parseInt(st.nextToken());
        // 수열 입력 받기
        array = Arrays.stream(br.readLine().split(" ")).map(el -> Integer.parseInt(el)).collect(Collectors.toList());

        // dp 배열 초기화
        dp = new int[lenOfArray];
        for (int i = 0; i < lenOfArray; i++) {
            dp[i] = array.get(i);
        }

        boolean isRemoved = false;
        for (int i = 1; i < lenOfArray; i++) {
            if (dp[i - 1] + array.get(i) <= dp[i]) {
                if (!isRemoved && i - 2 >= 0) {
                    if (dp[i] < dp[i - 2] + array.get(i)) {
                        dp[i] = dp[i - 2] + array.get(i);
                        isRemoved = true;
                    }
                }
            } else {
                dp[i] = dp[i - 1] + array.get(i);
            }
        }

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}