import java.util.*;
import java.io.*;

public class Main {
    static int rows, cols;
    static int[][] worlds;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14719_빗물\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        worlds = new int[rows][cols];
        st = new StringTokenizer(br.readLine());
        for (int col = 0; col < cols; col++) {
            int curHeight = Integer.parseInt(st.nextToken());
            for (int row = rows - 1; row >= rows - curHeight; row--) {
                worlds[row][col] = 1;
            }
        }

        // 제일 밑에서 부터 한 행씩 빗물 확인
        int answer = 0;
        for (int row = rows - 1; row >= 0; row--) {
            int tempSum = 0;
            boolean isStart = false;
            int curCol = 1;
            while (curCol < cols) {
                if (worlds[row][curCol - 1] == 1 && worlds[row][curCol] == 0) {
                    isStart = true;
                    tempSum += 1;
                } else if (isStart && worlds[row][curCol] == 0) {
                    tempSum += 1;
                }

                if (isStart && worlds[row][curCol] == 1) {
                    answer += tempSum;
                    tempSum = 0;
                    isStart = false;
                }
                curCol++;
            }
        }

        System.out.println(answer);
    }
}