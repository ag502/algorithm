import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int rows, cols, k;
    static int[][] matrix;
    static boolean[][] visited;
    static int answer = Integer.MIN_VALUE;

    static StringTokenizer st;

    public static void dfs(int curRow, int curCol, int curSum, int curCount) {
        visited[curRow][curCol] = true;
        curSum += matrix[curRow][curCol];

        if (curCount < k) {
            for (int nextRow = 0; nextRow < rows; nextRow++) {
                for (int nextCol = 0; nextCol < cols; nextCol++) {
                    boolean isClear = true;
                    for (int i = 0; i < movingDir.length; i++) {
                        int checkRow = nextRow + movingDir[i][0];
                        int checkCol = nextCol + movingDir[i][1];

                        if (0 <= checkRow && checkRow < rows && 0 <= checkCol && checkCol < cols) {
                            if (visited[nextRow][nextCol] || visited[checkRow][checkCol]) {
                                isClear = false;
                                break;
                            }
                        }
                    }

                    if (isClear) {
                        dfs(nextRow, nextCol, curSum, curCount + 1);
                    }
                }
            }
        }

        if (curCount == k) {
            answer = Math.max(answer, curSum);
        }
        visited[curRow][curCol] = false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_18290_NM과 K(1)\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        matrix = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                matrix[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new boolean[rows][cols];
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (!visited[row][col]) {
                    dfs(row, col, 0, 1);
                }
            }
        }

        System.out.println(answer);
    }
}