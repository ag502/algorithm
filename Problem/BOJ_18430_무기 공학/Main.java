import java.util.*;
import java.io.*;

public class Main {
    static int[][][] movingDir = { { { 0, 1 }, { 1, 0 } }, { { 0, -1 }, { 1, 0 } }, { { -1, 0 }, { 0, 1 } },
            { { 0, -1 }, { -1, 0 } } };
    static int rows, cols;
    static int[][] woods;
    static boolean[][] visited;
    static int answer = Integer.MIN_VALUE;

    static StringTokenizer st;

    public static boolean isInWoods(int firstRow, int firstCol, int secondRow, int secondCol) {
        if (0 > firstRow || rows <= firstRow || 0 > firstCol || cols <= firstCol) {
            return false;
        } else if (0 > secondRow || rows <= secondRow || 0 > secondCol || cols <= secondCol) {
            return false;
        }
        return true;
    }

    public static void dfs(int cRow, int cCol, int fRow, int fCol, int sRow, int sCol, int curSum) {
        visited[cRow][cCol] = true;
        visited[fRow][fCol] = true;
        visited[sRow][sCol] = true;

        int center = woods[cRow][cCol];
        int first = woods[fRow][fCol];
        int second = woods[sRow][sCol];

        curSum += center * 2 + first + second;

        for (int row = cRow; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (!visited[row][col]) {
                    for (int i = 0; i < movingDir.length; i++) {
                        int firstRow = row + movingDir[i][0][0];
                        int firstCol = col + movingDir[i][0][1];
                        int secondRow = row + movingDir[i][1][0];
                        int secondCol = col + movingDir[i][1][1];

                        if (isInWoods(firstRow, firstCol, secondRow, secondCol)) {
                            if (!visited[firstRow][firstCol] && !visited[secondRow][secondCol]) {
                                dfs(row, col, firstRow, firstCol, secondRow, secondCol, curSum);
                            }
                        }
                    }
                }
            }
        }

        // System.out.println("~~~~~~~~~~~~~~~~~~~");
        // for (int row = 0; row < rows; row++) {
        //     System.out.println(Arrays.toString(visited[row]));
        // }
        // System.out.println("~~~~~~~~~~~~~~~~~~~~");

        answer = Math.max(answer, curSum);
        visited[cRow][cCol] = false;
        visited[fRow][fCol] = false;
        visited[sRow][sCol] = false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_18430_무기 공학\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        woods = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                woods[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        // 부메랑 조합
        visited = new boolean[rows][cols];
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (!visited[row][col]) {
                    for (int i = 0; i < movingDir.length; i++) {
                        int firstRow = row + movingDir[i][0][0];
                        int firstCol = col + movingDir[i][0][1];
                        int secondRow = row + movingDir[i][1][0];
                        int secondCol = col + movingDir[i][1][1];

                        if (isInWoods(firstRow, firstCol, secondRow, secondCol)) {
                            if (!visited[firstRow][firstCol] && !visited[secondRow][secondCol]) {
                                dfs(row, col, firstRow, firstCol, secondRow, secondCol, 0);
                            }
                        }
                    }
                }
            }
        }

        System.out.println(answer == Integer.MIN_VALUE ? 0 : answer);
    }
}