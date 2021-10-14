import java.util.*;
import java.io.*;

public class Main {
    static int numOfStraw;

    static Integer[] straws;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1448_삼각형 만들기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfStraw = Integer.parseInt(br.readLine());
        straws = new Integer[numOfStraw];
        for (int straw = 0; straw < numOfStraw; straw++) {
            straws[straw] = Integer.parseInt(br.readLine());
        }

        // 빨대 내림차순 정렬
        Arrays.sort(straws, (a, b) -> b - a);

        int lengthOfTriangle = -1;
        for (int i = 0; i < numOfStraw - 2; i++) {
            int a = straws[i];
            int b = straws[i + 1];
            int c = straws[i + 2];

            if (a < b + c) {
                lengthOfTriangle = Math.max(lengthOfTriangle, a + b + c);
                break;
            }
        }
        System.out.println(lengthOfTriangle);
    }
}