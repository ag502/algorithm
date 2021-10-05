import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { -2, -1 }, { -2, 1 }, { -1, -2 }, { -1, 2 }, { 1, -2 }, { 1, 2 }, { 2, -1 },
            { 2, 1 } };

    static int rows;
    static int numOfEnemy;

    static int[][] chess;
    static boolean[][] visited;
    static int[][] dist;

    static int[] knightPos;
    static List<int[]> enemyPos;

    static StringTokenizer st;

    public static void bfs(int startRow, int startCol) {
        Queue<int[]> queue = new LinkedList<>();
        visited = new boolean[rows + 1][rows + 1];
        dist = new int[rows + 1][rows + 1];

        queue.offer(new int[] { startRow, startCol });
        visited[startRow][startCol] = true;
        dist[startRow][startCol] = 0;

        while (queue.size() != 0) {
            int[] curPos = queue.poll();

            for (int[] dir : movingDir) {
                int nextRow = curPos[0] + dir[0];
                int nextCol = curPos[1] + dir[1];

                if (1 <= nextRow && nextRow <= rows && 1 <= nextCol && nextCol <= rows) {
                    if (!visited[nextRow][nextCol]) {
                        queue.offer(new int[] { nextRow, nextCol });
                        visited[nextRow][nextCol] = true;
                        dist[nextRow][nextCol] = dist[curPos[0]][curPos[1]] + 1;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_18404_현명한 나이트\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        numOfEnemy = Integer.parseInt(st.nextToken());

        chess = new int[rows + 1][rows + 1];

        // knight 위치
        knightPos = new int[2];
        st = new StringTokenizer(br.readLine());
        knightPos[0] = Integer.parseInt(st.nextToken());
        knightPos[1] = Integer.parseInt(st.nextToken());

        // 상대 말 위치
        enemyPos = new ArrayList<>();
        for (int i = 0; i < numOfEnemy; i++) {
            st = new StringTokenizer(br.readLine());
            enemyPos.add(new int[] { Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()) });
        }

        // bfs
        bfs(knightPos[0], knightPos[1]);

        StringBuilder sb = new StringBuilder("");
        for (int[] pos : enemyPos) {
            sb.append(dist[pos[0]][pos[1]]);
            sb.append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}