import java.util.*;
import java.io.*;

public class Main {
    public static long gcd(long a, long b) {
        if (a % b == 0) {
            return b;
        }
        return gcd(b, a % b);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1850_최대공약수\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());

        long digitOfOne = gcd(a, b);

        StringBuilder answer = new StringBuilder("");

        for (int i = 0; i < digitOfOne; i++) {
            answer.append("1");
        }

        System.out.println(answer);
    }
}