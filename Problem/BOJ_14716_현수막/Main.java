import java.util.*;
import java.io.*;

public class Main {
    static int[][] checkDir = { { -1, 0 }, { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 }, { -1, -1 } };
    static int rows;
    static int cols;
    static int[][] flag;
    static boolean[][] visited;

    static StringTokenizer st;
    static int area = 0;

    public static void dfs(int curRow, int curCol) {
        // 방문
        visited[curRow][curCol] = true;

        // 갈 수 있는 곳 탐색
        for (int i = 0; i < checkDir.length; i++) {
            int nextRow = curRow + checkDir[i][0];
            int nextCol = curCol + checkDir[i][1];
            if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                if (flag[nextRow][nextCol] == 1 && !visited[nextRow][nextCol]) {
                    // 조건을 만족한다면 간다
                    dfs(nextRow, nextCol);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14716_현수막\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        // 현수막 초기화
        flag = new int[rows][cols];
        visited = new boolean[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                flag[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        // 시작점 찾기
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (flag[row][col] == 1 && !visited[row][col]) {
                    dfs(row, col);
                    area += 1;
                }
            }
        }

        System.out.println(area);
    }
}