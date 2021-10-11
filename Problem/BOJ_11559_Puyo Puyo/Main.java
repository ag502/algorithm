import java.util.*;
import java.io.*;

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    static char[] colors = { 'R', 'G', 'B', 'Y' };
    static int rows = 12;
    static int cols = 6;

    static char[][] board = new char[rows][cols];
    static boolean[][] visited;

    public static boolean puyoPop(int startRow, int startCol, char targetColor) {
        Queue<int[]> queue = new LinkedList<>();
        Queue<int[]> popPos = new LinkedList<>();

        queue.offer(new int[] { startRow, startCol });
        popPos.offer(new int[] { startRow, startCol });
        visited[startRow][startCol] = true;
        int count = 1;

        while (!queue.isEmpty()) {
            int[] curPos = queue.poll();

            for (int i = 0; i < movingDir.length; i++) {
                int nextRow = curPos[0] + movingDir[i][0];
                int nextCol = curPos[1] + movingDir[i][1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (!visited[nextRow][nextCol] && board[nextRow][nextCol] == targetColor) {
                        count += 1;
                        visited[nextRow][nextCol] = true;
                        queue.offer(new int[] { nextRow, nextCol });
                        popPos.offer(new int[] { nextRow, nextCol });
                    }
                }
            }
        }

        if (count >= 4) {
            while (!popPos.isEmpty()) {
                int[] curPopPos = popPos.poll();
                board[curPopPos[0]][curPopPos[1]] = '.';
            }
            return true;
        }
        return false;
    }

    public static void downShift() {
        for (int col = 0; col < cols; col++) {
            Queue<Character> queue = new LinkedList<>();
            for (int row = 0; row < rows; row++) {
                if (board[row][col] != '.') {
                    queue.offer(board[row][col]);
                }
            }

            int curStackSize = queue.size();
            for (int row = 0; row < rows - curStackSize; row++) {
                board[row][col] = '.';
            }

            for (int row = rows - curStackSize; row < rows; row++) {
                board[row][col] = queue.poll();
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_11559_Puyo Puyo\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        for (int row = 0; row < rows; row++) {
            char[] curRow = br.readLine().toCharArray();
            board[row] = curRow;
        }

        int answer = 0;
        while (true) {
            boolean isPop = false;

            visited = new boolean[rows][cols];
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    if (board[row][col] != '.' && !visited[row][col]) {
                        boolean result = puyoPop(row, col, board[row][col]);
                        if (!isPop && result) {
                            isPop = result;
                        }
                    }
                }
            }
            if (isPop) {
                answer += 1;
            } else {
                System.out.println(answer);
                return;
            }
            downShift();
        }
    }
}