import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int rows, cols;
    static char[][] fabric;

    public static boolean bfs(int startRow, int startCol) {
        Queue<int[]> positions = new LinkedList<>();
        boolean[][] visited = new boolean[rows][cols];

        positions.add(new int[] { startRow, startCol });
        visited[startRow][startCol] = true;

        while (!positions.isEmpty()) {
            int[] curPos = positions.poll();

            if (curPos[0] == rows - 1) {
                return true;
            }

            for (int i = 0; i < movingDir.length; i++) {
                int nextRow = curPos[0] + movingDir[i][0];
                int nextCol = curPos[1] + movingDir[i][1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (!visited[nextRow][nextCol] && fabric[nextRow][nextCol] == '0') {
                        visited[nextRow][nextCol] = true;
                        positions.add(new int[] { nextRow, nextCol });
                    }
                }
            }
        }

        return false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_13565_침투\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        fabric = new char[rows][cols];
        for (int row = 0; row < rows; row++) {
            fabric[row] = br.readLine().toCharArray();
        }

        for (int col = 0; col < cols; col++) {
            if (fabric[0][col] == '0') {
                boolean isPassed = bfs(0, col);
                if (isPassed == true) {
                    System.out.println("YES");
                    return;
                }
            }

        }
        System.out.println("NO");
    }
}