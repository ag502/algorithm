import java.util.*;
import java.io.*;

class Position {
    int row;
    int col;

    Position(int row, int col) {
        this.row = row;
        this.col = col;
    }
}

public class Main {
    static int[][] checkFourDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int rows;
    static int cols;
    static int[][] cheeze;
    static int sizeOfCheeze = 0;
    static boolean[][] air;
    static boolean[][] visited;

    static StringTokenizer st;

    public static void markAir() {
        Queue<Position> queue = new LinkedList<>();
        visited = new boolean[rows][cols];
        air = new boolean[rows][cols];

        queue.offer(new Position(0, 0));
        visited[0][0] = true;
        air[0][0] = true;

        while (queue.size() != 0) {
            Position curPos = queue.poll();

            for (int i = 0; i < checkFourDir.length; i++) {
                int nextRow = curPos.row + checkFourDir[i][0];
                int nextCol = curPos.col + checkFourDir[i][1];

                if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                    if (!visited[nextRow][nextCol] && cheeze[nextRow][nextCol] == 0) {
                        queue.offer(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                        air[nextRow][nextCol] = true;
                    }
                }
            }
        }
    }

    public static List<Position> getExposurePos() {
        List<Position> positions = new ArrayList<>();

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (cheeze[row][col] == 1) {
                    for (int i = 0; i < checkFourDir.length; i++) {
                        int nextRow = row + checkFourDir[i][0];
                        int nextCol = col + checkFourDir[i][1];
                        if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols
                                && air[nextRow][nextCol] == true) {
                            positions.add(new Position(row, col));
                            break;
                        }
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

        // 치즈 입력 받기
        cheeze = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                int curValue = Integer.parseInt(st.nextToken());
                cheeze[row][col] = curValue;
                if (curValue == 1) {
                    sizeOfCheeze += 1;
                }
            }
        }

        int time = 0;
        int prevSize = 0;

        while (sizeOfCheeze > 0) {
            time++;
            // 공기 표시
            markAir();
            // 지워야하는 위치 가져오기
            List<Position> positions = getExposurePos();

            // 지우기
            for (int i = 0; i < positions.size(); i++) {
                Position curPos = positions.get(i);
                cheeze[curPos.row][curPos.col] = 0;
            }

            prevSize = sizeOfCheeze;
            sizeOfCheeze -= positions.size();
        }

        System.out.println(time);
        System.out.println(prevSize);
    }
}