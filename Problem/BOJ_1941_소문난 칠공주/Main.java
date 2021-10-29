import java.util.*;
import java.io.*;

class Position {
    int row;
    int col;

    public Position(int row, int col) {
        this.row = row;
        this.col = col;
    }

    public String toString() {
        return this.row + "/" + this.col;
    }
}

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    static char[][] twoDStudents = new char[5][5];
    static char[] oneDStudents = new char[25];
    static boolean[][] checked = new boolean[5][5];
    static int answer = 0;

    public static boolean bfs() {
        Queue<Position> queue = new LinkedList<>();
        boolean[][] visited = new boolean[5][5];
        int area = 0;

        boolean flag = false;
        for (int row = 0; row < 5; row++) {
            for (int col = 0; col < 5; col++) {
                if (checked[row][col]) {
                    queue.add(new Position(row, col));
                    visited[row][col] = true;
                    flag = true;
                    break;
                }
            }
            if (flag) {
                break;
            }
        }

        while (!queue.isEmpty()) {
            Position curPos = queue.poll();

            for (int idx = 0; idx < movingDir.length; idx++) {
                int nextRow = curPos.row + movingDir[idx][0];
                int nextCol = curPos.col + movingDir[idx][1];

                if (0 <= nextRow && nextRow < 5 && 0 <= nextCol && nextCol < 5) {
                    if (!visited[nextRow][nextCol] && checked[nextRow][nextCol]) {
                        queue.add(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
            area += 1;
        }

        if (area == 7) {
            return true;
        }
        return false;
    }

    public static void dfs(int curIdx, int sCount, int yCount, int curCount) {
        int curRow = curIdx / 5;
        int curCol = curIdx % 5;
        checked[curRow][curCol] = true;

        if (oneDStudents[curIdx] == 'S') {
            sCount += 1;
        } else {
            yCount += 1;
        }

        if (curCount < 7) {
            for (int nextIdx = curIdx + 1; nextIdx < 25; nextIdx++) {
                dfs(nextIdx, sCount, yCount, curCount + 1);
            }
        }

        if (curCount == 7) {
            if (sCount >= 4 && bfs()) {
                answer += 1;
            }
        }

        checked[curRow][curCol] = false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1941_소문난 칠공주\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        for (int row = 0; row < 5; row++) {
            twoDStudents[row] = br.readLine().toCharArray();
            for (int col = 0; col < 5; col++) {
                oneDStudents[row * 5 + col] = twoDStudents[row][col];
            }
        }

        for (int idx = 0; idx < 25; idx++) {
            dfs(idx, 0, 0, 1);
        }

        System.out.println(answer);
    }
}