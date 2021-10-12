import java.io.*;
import java.util.*;

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 0, -1 }, { 1, 0 }, { 0, 1 } };
    static int rows;
    static int ateFish = 0;
    static int sharkSize = 2;
    static int time = 0;

    static int[][] sea;
    static int[] curSharkPos = new int[2];

    static StringTokenizer st;

    public static boolean isCallMom() {
        int numOfBlank = 0;
        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < rows; col++) {
                if (sea[row][col] != 9 && (sea[row][col] == 0 || sea[row][col] >= sharkSize)) {
                    numOfBlank += 1;
                }
            }
        }

        return rows * rows - 1 == numOfBlank ? true : false;
    }

    public static int babySharkMoving() {
        Queue<int[]> queue = new LinkedList<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] < o2[0]) {
                    return -1;
                } else if (o1[0] > o2[0]) {
                    return 1;
                } else {
                    return o1[1] - o2[1];
                }
            }
        });
        boolean[][] visited = new boolean[rows][rows];

        pq.offer(curSharkPos);
        visited[curSharkPos[0]][curSharkPos[1]] = true;
        int temp = 0;

        while (!pq.isEmpty()) {
            int curQueueSize = pq.size();
            temp += 1;
            for (int size = 0; size < curQueueSize; size++) {
                int[] curPos = pq.poll();
                int curState = sea[curPos[0]][curPos[1]];

                // 상어가 먹을 수 있는 물고기 일때
                if (curState != 0 && curState != 9 && sharkSize > curState) {
                    ateFish += 1;
                    // 상어의 출발지 갱신
                    sea[curSharkPos[0]][curSharkPos[1]] = 0;
                    sea[curPos[0]][curPos[1]] = 9;
                    curSharkPos[0] = curPos[0];
                    curSharkPos[1] = curPos[1];

                    if (sharkSize == ateFish) {
                        sharkSize += 1;
                        ateFish = 0;
                    }
                    // System.out.println(curPos[0] + "//" + curPos[1]);
                    return temp - 1;
                }

                queue.offer(curPos);
            }

            // 먹을 수 있는 물고기가 없을 때
            while (!queue.isEmpty()) {
                int[] curPos = queue.poll();

                for (int i = 0; i < movingDir.length; i++) {
                    int nextRow = curPos[0] + movingDir[i][0];
                    int nextCol = curPos[1] + movingDir[i][1];

                    if (0 <= nextRow && nextRow < rows && 0 <= nextCol && nextCol < rows) {
                        if (!visited[nextRow][nextCol] && 0 <= sea[nextRow][nextCol]
                                && sea[nextRow][nextCol] <= sharkSize) {
                            pq.offer(new int[] { nextRow, nextCol });
                            visited[nextRow][nextCol] = true;
                        }
                    }
                }
            }

        }
        return -1;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_16236_아기 상어\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        rows = Integer.parseInt(br.readLine());
        sea = new int[rows][rows];

        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < rows; col++) {
                int curState = Integer.parseInt(st.nextToken());
                sea[row][col] = curState;
                if (curState == 9) {
                    curSharkPos[0] = row;
                    curSharkPos[1] = col;
                }
            }
        }

        while (true) {
            int result = babySharkMoving();
            if (result != -1) {
                time += result;
            } else {
                break;
            }
        }

        System.out.println(time);
    }
}