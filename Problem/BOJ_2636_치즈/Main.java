import java.util.*;
import java.io.*;

class Position {
    int row;
    int col;

    Position(int row, int col) {
        this.row = row;
        this.col = col;
    }

    @Override
    public String toString() {
        return "( " + this.row + ", " + this.col + " )";
    }
}

public class Main {
    static int[][] checkFourDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int[][] checkEightDir = { { -1, 0 }, { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 },
            { -1, -1 }, { -1, 0 } };
    static int rows;
    static int cols;
    static int sizeOfCheeze = 0;
    static int[][] cheeze;
    static boolean[][] visited;

    static StringTokenizer st;

    public static boolean isPossible(int curRow, int curCol) {
        for (int i = 0; i < checkFourDir.length; i++) {
            int nextRow = curRow + checkFourDir[i][0];
            int nextCol = curCol + checkFourDir[i][1];
            if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                if (cheeze[nextRow][nextCol] == 3) {
                    return true;
                }
            }
        }
        return false;
    }

    public static void markAir(int curRow, int curCol) {
        // 방문
        cheeze[curRow][curCol] = 3;
        // 가능한 곳 탐색
        for (int i = 0; i < checkFourDir.length; i++) {
            int nextRow = curRow + checkFourDir[i][0];
            int nextCol = curCol + checkFourDir[i][1];
            if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                if (cheeze[nextRow][nextCol] == 0 && isPossible(nextRow, nextCol)) {
                    markAir(nextRow, nextCol);
                }
            }
        }
    }

    public static List<Position> getExposurePos(int curRow, int curCol) {
        List<Position> positions = new ArrayList<>();
        Queue<Position> queue = new LinkedList<>();

        // 처음 위치 방문
        queue.offer(new Position(curRow, curCol));
        visited[curRow][curCol] = true;

        while (queue.size() != 0) {
            Position curPos = queue.poll();
            positions.add(new Position(curPos.row, curPos.col));

            // 갈 수 있는 곳 확인
            for (int i = 0; i < checkEightDir.length; i++) {
                int nextRow = curPos.row + checkEightDir[i][0];
                int nextCol = curPos.col + checkEightDir[i][1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (!visited[nextRow][nextCol] && isPossible(nextRow, nextCol) && cheeze[nextRow][nextCol] == 1) {
                        queue.offer(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                    }
                }
            }
        }
        return positions;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2636_치즈\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        // 초기 cheeze 입력
        cheeze = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                int curValue = Integer.parseInt(st.nextToken());
                cheeze[row][col] = curValue;
                if (curValue == 1) {
                    sizeOfCheeze++;
                }
            }
        }

        cheeze[0][0] = 3;
        int prevSize = 0;
        int time = 0;
        while (sizeOfCheeze > 0) {
            time++;
            // 공기 부분 '3'으로 표시
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    if (cheeze[row][col] == 0 && isPossible(row, col)) {
                        markAir(row, col);
                    }
                }
            }

            // 공기와 접촉된 부분 좌표 얻어오기
            visited = new boolean[rows][cols];
            List<List<Position>> positions = new ArrayList<>();
            for (int row = 0; row < rows; row++) {
                for (int col = 0; col < cols; col++) {
                    if (!visited[row][col] && cheeze[row][col] == 1 && isPossible(row, col)) {
                        positions.add(getExposurePos(row, col));
                    }
                }
            }

            if (positions.size() != 0) {
                prevSize = sizeOfCheeze;
                for (int i = 0; i < positions.size(); i++) {
                    // System.out.println(positions.get(i).size());
                    sizeOfCheeze -= positions.get(i).size();
                    for (int j = 0; j < positions.get(i).size(); j++) {
                        Position curPos = positions.get(i).get(j);
                        cheeze[curPos.row][curPos.col] = 3;
                    }

                }
            }
        }
        System.out.println(time);
        System.out.println(prevSize);
    }
}