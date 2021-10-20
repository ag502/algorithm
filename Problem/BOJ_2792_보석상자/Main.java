import java.util.*;
import java.io.*;

public class Main {
    static int numOfStudents, numOfColors;
    static int[] jewelry;

    public static int getMaxNumOfJewels() {
        int result = -1;
        int left = 1;
        int right = 1000000000;

        while (left <= right) {
            int mid = (left + right) / 2;
            // 나눠줄 수 있는 학생수 구하기
            long curStudents = 0;
            for (int curJewelCount : jewelry) {
                int jewelPerStudent = curJewelCount / mid;
                int numOfRemainsJewel = curJewelCount % mid;

                curStudents += jewelPerStudent;
                if (numOfRemainsJewel != 0) {
                    curStudents += 1;
                }
            }

            if (curStudents <= numOfStudents) {
                right = mid - 1;
                result = mid;
            } else {
                left = mid + 1;
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2792_보석상자\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        numOfStudents = Integer.parseInt(st.nextToken());
        numOfColors = Integer.parseInt(st.nextToken());

        jewelry = new int[numOfColors];
        for (int i = 0; i < numOfColors; i++) {
            jewelry[i] = Integer.parseInt(br.readLine());
        }

        System.out.println(getMaxNumOfJewels());
    }
}