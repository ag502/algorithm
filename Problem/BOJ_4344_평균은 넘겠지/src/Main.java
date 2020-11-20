import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            int avg = 0;
            StringTokenizer st = new StringTokenizer(br.readLine());

            int numOfStudent = Integer.parseInt(st.nextToken());
            int [] studentScore = new int[numOfStudent];

            for (int j = 0; j < numOfStudent; j++) {
                int score = Integer.parseInt(st.nextToken());
                avg += score;
                studentScore[j] = score;
            }
            avg = avg / numOfStudent;

            int overTheAvg = 0;
            for (int j = 0; j < studentScore.length; j++) {
                if (studentScore[j] > avg) {
                    overTheAvg += 1;
                }
            }
            System.out.printf("%.3f", (float) (overTheAvg * 100 / (float) studentScore.length));
            System.out.println("%");
        }
    }
}
