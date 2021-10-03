import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    static int rows;
    static int cols;

    static List<String[]> farm;
    static boolean visited[][];
    static int numOfWolves = 0;
    static int numOfSheeps = 0;

    public static void dfs(int curRow, int curCol) {
        visited[curRow][curCol] = true;
        String curState = farm.get(curRow)[curCol];

        if (curState.equals("v")) {
            numOfWolves += 1;
        } else if (curState.equals("o")) {
            numOfSheeps += 1;
        }

        for (int i = 0; i < movingDir.length; i++) {
            int nextRow = curRow + movingDir[i][0];
            int nextCol = curCol + movingDir[i][1];

            if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                if (!visited[nextRow][nextCol] && !farm.get(nextRow)[nextCol].equals("#")) {
                    dfs(nextRow, nextCol);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_3184_양\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        farm = new ArrayList<>();
        for (int row = 0; row < rows; row++) {
            farm.add(br.readLine().split(""));
        }

        visited = new boolean[rows][cols];
        int answerWolves = 0;
        int answerSheeps = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (!farm.get(row)[col].equals("#") && !visited[row][col]) {
                    numOfSheeps = 0;
                    numOfWolves = 0;
                    dfs(row, col);

                    if (numOfWolves >= numOfSheeps) {
                        answerWolves += numOfWolves;
                    } else {
                        answerSheeps += numOfSheeps;
                    }
                }
            }
        }

        System.out.println(answerSheeps + " " + answerWolves);
    }
}