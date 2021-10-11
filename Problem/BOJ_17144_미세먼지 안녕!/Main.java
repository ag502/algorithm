import java.util.*;
import java.io.*;

public class Main {
    static int[][] spreadDir = { { -1, 0 }, { 1, 0 }, { 0, -1 }, { 0, 1 } };
    static int rows, cols, time;

    static int[][] room;
    static List<int[]> airCleanerPos = new ArrayList<>();

    static StringTokenizer st;

    public static void spreadDust() {
        int[][] tempRoom = new int[rows][cols];
        tempRoom[airCleanerPos.get(0)[0]][airCleanerPos.get(0)[1]] = -1;
        tempRoom[airCleanerPos.get(1)[0]][airCleanerPos.get(1)[1]] = -1;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (room[row][col] > 0) {
                    Queue<int[]> pos = new LinkedList<>();
                    for (int i = 0; i < spreadDir.length; i++) {
                        int nextRow = row + spreadDir[i][0];
                        int nextCol = col + spreadDir[i][1];

                        // 4 방향 확인
                        if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < cols) {
                            if (room[nextRow][nextCol] != -1) {
                                pos.offer(new int[] { nextRow, nextCol });
                            }
                        }
                    }

                    int aside = room[row][col] / 5;
                    int center = room[row][col] - (aside * pos.size());

                    // 값변경
                    tempRoom[row][col] += center;
                    while (!pos.isEmpty()) {
                        int[] curPos = pos.poll();
                        tempRoom[curPos[0]][curPos[1]] += aside;
                    }
                }
            }
        }

        // 확산값 원래 배열에 대입
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                room[row][col] = tempRoom[row][col];
            }
        }
    }

    public static void cleanAir() {
        // 위쪽 반시계 방향
        int upperRow = airCleanerPos.get(0)[0];
        int upperCol = airCleanerPos.get(0)[1];

        for (int row = upperRow - 1; row > 0; row--) {
            room[row][0] = room[row - 1][0];
        }

        for (int col = 1; col < cols; col++) {
            room[0][col - 1] = room[0][col];
        }

        for (int row = 1; row <= upperRow; row++) {
            room[row - 1][cols - 1] = room[row][cols - 1];
        }

        for (int col = cols - 2; col >= 1; col--) {
            room[upperRow][col + 1] = room[upperRow][col];
        }
        room[upperRow][1] = 0;

        // 아래쪽 시계 방향
        int lowerRow = airCleanerPos.get(1)[0];
        int lowerCol = airCleanerPos.get(1)[1];

        for (int row = lowerRow + 2; row < rows; row++) {
            room[row - 1][0] = room[row][0];
        }

        for (int col = 1; col < cols; col++) {
            room[rows - 1][col - 1] = room[rows - 1][col];
        }

        for (int row = rows - 2; row >= lowerRow; row--) {
            room[row + 1][cols - 1] = room[row][cols - 1];
        }

        for (int col = cols - 2; col >= 1; col--) {
            room[lowerRow][col + 1] = room[lowerRow][col];
        }
        room[lowerRow][1] = 0;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_17144_미세먼지 안녕!\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input;
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());
        time = Integer.parseInt(st.nextToken());

        // 방 초기화
        room = new int[rows][cols];
        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                int curState = Integer.parseInt(st.nextToken());
                room[row][col] = curState;
                if (curState == -1) {
                    airCleanerPos.add(new int[] { row, col });
                }
            }
        }

        while (time != 0) {
            time--;
            spreadDust();
            cleanAir();
        }

        int answer = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                if (room[row][col] > 0) {
                    answer += room[row][col];
                }
            }
        }

        System.out.println(answer);
    }
}