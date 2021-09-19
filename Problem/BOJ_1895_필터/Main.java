import java.util.*;
import java.io.*;

public class Main {
    static int rows;
    static int cols;
    static int[][] image;
    static StringTokenizer st;

    public static int getMediumValue(int curRow, int curCol) {
        List<Integer> filter = new ArrayList<>();
        for (int i = curRow; i <= curRow + 2; i++) {
            for (int j = curCol; j <= curCol + 2; j++) {
                filter.add(image[i][j]);
            }
        }
        Collections.sort(filter);
        return filter.get(4);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1895_필터\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        image = new int[rows][cols];
        // 이미지 배열 초기화
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                image[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        int targetNumber = Integer.parseInt(br.readLine());

        int answer = 0;
        // 이미지 필터 적용
        for (int row = 0; row < rows - 2; row++) {
            for (int col = 0; col < cols - 2; col++) {
                int mediumValue = getMediumValue(row, col);
                if (targetNumber <= mediumValue) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}
