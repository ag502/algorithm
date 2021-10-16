import java.util.*;
import java.io.*;

class Position {
    int row;
    int col;

    public Position(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

public class Main {
    static int[][] oddRowDir = { { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 0, -1 }, { -1, 0 } };
    static int[][] evenRowDir = { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 1, -1 }, { 0, -1 }, { -1, -1 } };

    static int rows, cols;
    static int[][] walls;
    static boolean[][] visited;
    static int answer = 0;
    static StringTokenizer st;

    public static void markVacancy() {
        Queue<Position> queue = new LinkedList<>();
        queue.add(new Position(0, 0));
        walls[0][0] = 3;
        visited[0][0] = true;

        while (!queue.isEmpty()) {
            Position curPos = queue.poll();

            for (int idx = 0; idx < evenRowDir.length; idx++) {
                int nextRow = 0;
                int nextCol = 0;

                if (curPos.row % 2 == 0) {
                    nextRow = curPos.row + evenRowDir[idx][0];
                    nextCol = curPos.col + evenRowDir[idx][1];
                } else {
                    nextRow = curPos.row + oddRowDir[idx][0];
                    nextCol = curPos.col + oddRowDir[idx][1];
                }

                if (0 <= nextRow && nextRow < rows + 2 && 0 <= nextCol && nextCol < cols + 2) {
                    if (!visited[nextRow][nextCol] && walls[nextRow][nextCol] == 0) {
                        walls[nextRow][nextCol] = 3;
                        queue.offer(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
        }
    }

    public static void bfs(int startRow, int startCol) {
        Queue<Position> queue = new LinkedList<>();
        queue.add(new Position(startRow, startCol));
        visited[startRow][startCol] = true;

        while (!queue.isEmpty()) {
            Position curPos = queue.poll();

            for (int idx = 0; idx < evenRowDir.length; idx++) {
                int nextRow = 0;
                int nextCol = 0;

                if (curPos.row % 2 == 0) {
                    nextRow = curPos.row + evenRowDir[idx][0];
                    nextCol = curPos.col + evenRowDir[idx][1];
                } else {
                    nextRow = curPos.row + oddRowDir[idx][0];
                    nextCol = curPos.col + oddRowDir[idx][1];
                }

                if (0 <= nextRow && nextRow < rows + 2 && 0 <= nextCol && nextCol < cols + 2) {
                    if (walls[nextRow][nextCol] == 3) {
                        answer += 1;
                    }
                    if (!visited[nextRow][nextCol] && walls[nextRow][nextCol] == 1) {
                        queue.offer(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_5547_일루미네이션\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        cols = Integer.parseInt(st.nextToken());
        rows = Integer.parseInt(st.nextToken());

        // 벽면 입력
        walls = new int[rows + 2][cols + 2];
        for (int row = 1; row <= rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 1; col <= cols; col++) {
                walls[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        visited = new boolean[rows + 2][cols + 2];
        // 겉부분 숫자 변경
        markVacancy();

        // for (int row = 0; row < rows + 2; row++) {
        // System.out.println(Arrays.toString(walls[row]));
        // }

        // 둘레 길이 측정
        visited = new boolean[rows + 2][cols + 2];
        for (int row = 1; row <= rows; row++) {
            for (int col = 1; col <= cols; col++) {
                if (walls[row][col] == 1 && !visited[row][col]) {
                    bfs(row, col);
                }
            }
        }
        System.out.println(answer);
    }
}