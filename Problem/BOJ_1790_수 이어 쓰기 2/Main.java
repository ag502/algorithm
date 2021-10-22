import java.util.*;
import java.io.*;

public class Main {
    static int n, k;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1790_수 이어 쓰기 2\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());

        String number = st.nextToken();
        n = Integer.parseInt(number);
        int maxLength = number.length();

        k = Integer.parseInt(st.nextToken());

        // 몇자리 수인지 확인
        long nth = 0;
        int targetLength = -1;
        for (int i = 1; i <= maxLength; i++) {
            nth += i * 9 * Math.pow(10, i - 1);
            if (nth >= k) {
                targetLength = i;
                break;
            }
        }

        // 현재 해당하는 자릿수 시작
        long start = nth - (targetLength * 9 * (long) Math.pow(10, targetLength - 1)) + 1;
        int count = 0;
        while (start <= k) {
            start += targetLength;
            count += 1;
        }

        int targetNumber = (int) Math.pow(10, targetLength - 1) + (count - 1);

        if (targetNumber > n) {
            System.out.println(-1);
            return;
        }

        int idx = (int) (k - (start - targetLength));
        System.out.println(Integer.toString(targetNumber).charAt(idx));

    }
}