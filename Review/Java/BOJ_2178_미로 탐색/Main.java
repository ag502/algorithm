import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
    static int rows;
    static int cols;

    static char[][] maze;
    static int[][] dist;
    static boolean[][] visited;

    public static void bfs(int startRow, int startCol) {
        Queue<int[]> queue = new LinkedList<>();
        visited = new boolean[rows][cols];
        dist = new int[rows][cols];

        queue.offer(new int[] { 0, 0 });
        dist[0][0] = 1;
        visited[0][0] = true;

        while (queue.size() != 0) {
            int[] curPos = queue.poll();
            int curRow = curPos[0];
            int curCol = curPos[1];

            if (curRow == rows - 1 && curCol == cols - 1) {
                break;
            }

            for (int[] dir : movingDir) {
                int nextRow = curRow + dir[0];
                int nextCol = curCol + dir[1];
                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (!visited[nextRow][nextCol] && maze[nextRow][nextCol] == '1') {
                        queue.offer(new int[] { nextRow, nextCol });
                        visited[nextRow][nextCol] = true;
                        dist[nextRow][nextCol] = dist[curRow][curCol] + 1;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_2178_미로 탐색\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        maze = new char[rows][cols];
        for (int row = 0; row < rows; row++) {
            char[] curRow = br.readLine().toCharArray();
            maze[row] = curRow;
        }

        // bfs
        bfs(0, 0);

        System.out.println(dist[rows - 1][cols - 1]);
    }
}