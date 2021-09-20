import java.util.*;
import java.io.*;

public class Main {
    static int[][] checkDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 }, };
    static int rows;
    static int cols;
    static int[][] originalCells;
    static int[][] vaccineCells;
    static boolean[][] originalVisited;

    static StringTokenizer st;

    public static boolean isPossible() {
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (originalCells[row][col] != vaccineCells[row][col]) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void dfs(int curRow, int curCol, int curValue, int target) {
        // 방문
        originalVisited[curRow][curCol] = true;
        originalCells[curRow][curCol] = target;

        // 갈 수 있는 곳 확인
        for (int i = 0; i < checkDir.length; i++) {
            int nextRow = curRow + checkDir[i][0];
            int nextCol = curCol + checkDir[i][1];
            if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                if (originalCells[nextRow][nextCol] == curValue && !originalVisited[nextRow][nextCol]) {
                    dfs(nextRow, nextCol, curValue, target);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_22352_항체 인식\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        // 세포 초기화
        originalCells = new int[rows][cols];
        originalVisited = new boolean[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                originalCells[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        vaccineCells = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                vaccineCells[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        for (int row = 0; row < rows; row++) {
            boolean flag = false;
            for (int col = 0; col < cols; col++) {
                if (originalCells[row][col] != vaccineCells[row][col]) {
                    flag = true;
                    dfs(row, col, originalCells[row][col], vaccineCells[row][col]);
                    break;
                }
            }
            if (flag) {
                break;
            }
        }

        if (isPossible()) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}