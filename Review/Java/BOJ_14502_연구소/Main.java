import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };
    static int rows;
    static int cols;

    static int[][] labs;
    static StringTokenizer st;
    static List<int[]> virusPos;
    static boolean[][] visited;
    static int numOfWalls = 0;
    static int infectionArea = Integer.MAX_VALUE;

    static int a = 0;

    public static void infection() {
        int area = 0;
        Queue<int[]> queue = new LinkedList<>();
        visited = new boolean[rows][cols];

        // 바이러스 위치 삽입
        for (int i = 0; i < virusPos.size(); i++) {
            int[] curPos = virusPos.get(i);
            queue.offer(curPos);
            visited[curPos[0]][curPos[1]] = true;
        }

        while (queue.size() != 0) {
            int[] curPos = queue.poll();
            area += 1;

            for (int[] dir : movingDir) {
                int nextRow = curPos[0] + dir[0];
                int nextCol = curPos[1] + dir[1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (!visited[nextRow][nextCol] && labs[nextRow][nextCol] == 0) {
                        queue.offer(new int[] { nextRow, nextCol });
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
        }

        infectionArea = Math.min(infectionArea, area);
    }

    public static void makeWalls(int curRow, int curCol, int count) {
        labs[curRow][curCol] = 1;

        if (count < 3) {
            for (int row = curRow; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    if (labs[row][col] == 0) {
                        makeWalls(row, col, count + 1);
                    }
                }
            }
        }

        if (count == 3) {
            infection();
        }
        labs[curRow][curCol] = 0;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_14502_연구소\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        labs = new int[rows][cols];
        virusPos = new ArrayList<>();
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                int curState = Integer.parseInt(st.nextToken());
                labs[row][col] = curState;
                if (curState == 2) {
                    virusPos.add(new int[] { row, col });
                } else if (labs[row][col] == 1) {
                    numOfWalls += 1;
                }
            }
        }

        // 벽 만들기
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (labs[row][col] == 0) {
                    makeWalls(row, col, 1);
                }
            }
        }

        // System.out.println(infectionArea);
        System.out.println((rows * cols) - infectionArea - numOfWalls - 3);
    }
}