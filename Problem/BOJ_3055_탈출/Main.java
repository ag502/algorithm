import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    static int rows;
    static int cols;

    static char[][] forest;
    static int[][] dist;
    static int[] hedgeDogPos = new int[2];
    static int[] cavePos = new int[2];
    static StringTokenizer st;

    public static void drain() {
        Queue<int[]> queue = new LinkedList<>();

        // 물 찾기
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (forest[row][col] == '*') {
                    queue.offer(new int[] { row, col });
                }
            }
        }

        // 침수
        while (queue.size() != 0) {
            int[] curPos = queue.poll();

            for (int[] dir : movingDir) {
                int nextRow = curPos[0] + dir[0];
                int nextCol = curPos[1] + dir[1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (forest[nextRow][nextCol] == '.') {
                        forest[nextRow][nextCol] = '*';
                    }
                }
            }
        }

        // for (int row = 0; row < rows; row++) {
        // System.out.println(Arrays.toString(forest[row]));
        // }
        // System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!");
    }

    public static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        dist = new int[rows][cols];
        boolean[][] visited = new boolean[rows][cols];

        queue.offer(hedgeDogPos);
        visited[hedgeDogPos[0]][hedgeDogPos[1]] = true;

        while (queue.size() != 0) {
            // 침수
            drain();

            int curSize = queue.size();

            for (int size = 0; size < curSize; size++) {
                int[] curPos = queue.poll();
                if (forest[curPos[0]][curPos[1]] == 'D') {
                    break;
                }

                for (int[] dir : movingDir) {
                    int nextRow = curPos[0] + dir[0];
                    int nextCol = curPos[1] + dir[1];

                    if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                        // System.out.println(nextRow + " // " + nextCol);
                        if (!visited[nextRow][nextCol] && forest[nextRow][nextCol] != '*'
                                && forest[nextRow][nextCol] != 'X') {
                            queue.offer(new int[] { nextRow, nextCol });
                            visited[nextRow][nextCol] = true;
                            dist[nextRow][nextCol] = dist[curPos[0]][curPos[1]] + 1;
                        }

                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_3055_탈출\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        forest = new char[rows][cols];
        for (int row = 0; row < rows; row++) {
            char[] curRow = br.readLine().toCharArray();
            for (int col = 0; col < cols; col++) {
                forest[row][col] = curRow[col];
                // 고슴도치 위치
                if (curRow[col] == 'S') {
                    hedgeDogPos[0] = row;
                    hedgeDogPos[1] = col;
                }
                // 목적지 위치
                else if (curRow[col] == 'D') {
                    cavePos[0] = row;
                    cavePos[1] = col;
                }
            }
        }

        bfs();
        int answer = dist[cavePos[0]][cavePos[1]];
        System.out.println(answer == 0 ? "KAKTUS" : answer);
    }
}
