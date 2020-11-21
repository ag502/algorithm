import java.io.*;
import java.lang.reflect.Array;
import java.util.*;

public class Main {
    static int testCase;
    static int[][] movingDir = {{-2, 1}, {-1, 2}, {1, 2}, {2, 1}, {2, -1}, {1, -2}, {-1, -2}, {-2, -1}};

    public static int bfs(boolean[][] board, int startRow, int startCol, int finishRow, int finishCol, int width) {
        Queue<int[]> queue = new LinkedList<>();
        int [] initPos = {startRow, startCol};
        queue.add(initPos);
        board[startRow][startCol] = true;

        int count = 0;

        while (queue.size() != 0) {
            int curSize = queue.size();

            for (int i = 0; i < curSize; i++) {
                int [] curPos = queue.poll();

                if (curPos[0] == finishRow && curPos[1] == finishCol) {
                    return count;
                }

                for (int [] dist : movingDir) {
                    int nextRow = curPos[0] + dist[0];
                    int nextCol = curPos[1] + dist[1];

                    if ((0 <= nextRow && nextRow < width) && (0 <= nextCol && nextCol < width)) {
                        if (!board[nextRow][nextCol]) {
                            int [] nextPos = {nextRow, nextCol};
                            queue.add(nextPos);
                            board[nextRow][nextCol] = true;
                        }
                    }
                }
            }
            count++;
        }
        return 0;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        testCase = Integer.parseInt(br.readLine());

        for (int t = 0; t < testCase; t++) {
                int width = Integer.parseInt(br.readLine());
                boolean[][] chessBoard = new boolean[width][width];

                StringTokenizer st = new StringTokenizer(br.readLine());
                int startRow = Integer.parseInt(st.nextToken());
                int startCol = Integer.parseInt(st.nextToken());

                st = new StringTokenizer(br.readLine());
                int finishRow = Integer.parseInt(st.nextToken());
                int finishCol = Integer.parseInt(st.nextToken());
                int count = bfs(chessBoard, startRow, startCol, finishRow, finishCol, width);
                System.out.println(count);
            }
    }
}
