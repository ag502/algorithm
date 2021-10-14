import java.util.*;
import java.io.*;

public class Main {
    static int numOfStairs;
    static int[] stairs;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2846_오르막길\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfStairs = Integer.parseInt(br.readLine());

        stairs = new int[numOfStairs];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < numOfStairs; i++) {
            stairs[i] = Integer.parseInt(st.nextToken());
        }

        // 오르막 길 계산
        int leftPtr = 0;
        int rightPtr = 1;
        int sizeOfSlide = 0;

        while (leftPtr < numOfStairs && rightPtr < numOfStairs) {
            if (stairs[rightPtr - 1] >= stairs[rightPtr]) {
                sizeOfSlide = Math.max(sizeOfSlide, stairs[rightPtr - 1] - stairs[leftPtr]);

                leftPtr = rightPtr;
                rightPtr += 1;
                continue;
            }
            rightPtr += 1;
        }

        sizeOfSlide = Math.max(sizeOfSlide, stairs[rightPtr - 1] - stairs[leftPtr]);
        System.out.println(sizeOfSlide);
    }
}