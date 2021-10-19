import java.util.*;
import java.io.*;

public class Main {
    static int numOfNephews, numOfCookies;
    static int[] cookieLengths;

    static StringTokenizer st;

    public static int getCookieLength() {
        int result = 1000000001;
        int left = 1;
        int right = 1000000000;

        while (left <= right) {
            int mid = (left + right) / 2;

            // 나눠 줄 수 있는 조카 수
            int curNephews = 0;
            for (int i = 0; i < numOfCookies; i++) {
                if (mid <= cookieLengths[i]) {
                    curNephews += cookieLengths[i] / mid;
                }
            }

            if (curNephews < numOfNephews) {
                right = mid - 1;
            } else {
                left = mid + 1;
                result = mid;
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_16401_과자 나눠주기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfNephews = Integer.parseInt(st.nextToken());
        numOfCookies = Integer.parseInt(st.nextToken());

        cookieLengths = new int[numOfCookies];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < numOfCookies; i++) {
            cookieLengths[i] = Integer.parseInt(st.nextToken());
        }

        // 정렬
        Arrays.sort(cookieLengths);

        int answer = getCookieLength();
        System.out.println(answer == 1000000001 ? 0 : answer);
    }
}