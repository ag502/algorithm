import java.util.*;
import java.io.*;

public class Main {
    static Map<Integer, int[]> movingDir = new HashMap<>() {
        {
            put(0, new int[] { 0, 1 });
            put(1, new int[] { -1, 0 });
            put(2, new int[] { 0, -1 });
            put(3, new int[] { 1, 0 });
        }
    };
    static Map<Integer, Integer> rotateDir = new HashMap<>() {
        {
            put(0, 1);
            put(1, 2);
            put(3, 0);
            put(2, 3);
        }
    };
    static int numOfCurves;
    static boolean[][] pos = new boolean[101][101];

    static StringTokenizer st;

    public static int checkSquare() {
        int numOfSquares = 0;
        int[][] squareDir = { { 0, 1 }, { 1, 1 }, { 1, 0 } };

        for (int row = 0; row < 101; row++) {
            for (int col = 0; col < 101; col++) {
                if (pos[row][col]) {
                    int count = 0;

                    // 나머지 꼭지점 확인
                    for (int i = 0; i < squareDir.length; i++) {
                        int nextRow = row + squareDir[i][0];
                        int nextCol = col + squareDir[i][1];

                        if (nextRow < 101 && nextCol < 101) {
                            if (pos[nextRow][nextCol]) {
                                count += 1;
                            }
                        }
                    }

                    if (count >= 3) {
                        numOfSquares += 1;
                    }
                }
            }
        }

        return numOfSquares;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_15685_드래곤 커브\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfCurves = Integer.parseInt(br.readLine());

        for (int i = 0; i < numOfCurves; i++) {
            st = new StringTokenizer(br.readLine());

            // 드래곤 커브 표시
            int col = Integer.parseInt(st.nextToken());
            int row = Integer.parseInt(st.nextToken());
            int curDir = Integer.parseInt(st.nextToken());
            int gen = Integer.parseInt(st.nextToken());

            int[] standardPos = { row, col };
            Deque<Integer> originalDir = new ArrayDeque<>();
            Deque<Integer> newDir = new ArrayDeque<>();

            // 0세대
            pos[standardPos[0]][standardPos[1]] = true;
            standardPos[0] += movingDir.get(curDir)[0];
            standardPos[1] += movingDir.get(curDir)[1];
            pos[standardPos[0]][standardPos[1]] = true;
            originalDir.addLast(curDir);

            // 나머지 세대
            while (gen != 0) {
                gen--;
                if (originalDir.size() == 0) {
                    Deque<Integer> temp = originalDir;
                    originalDir = newDir;
                    newDir = temp;
                }

                int curSize = originalDir.size();
                for (int size = 0; size < curSize; size++) {
                    int originDir = originalDir.removeFirst();
                    int newRotateDir = rotateDir.get(originDir);

                    int nextRow = standardPos[0] + movingDir.get(newRotateDir)[0];
                    int nextCol = standardPos[1] + movingDir.get(newRotateDir)[1];

                    if (0 <= nextRow && nextRow < 101 && 0 <= nextCol && nextCol < 101) {
                        standardPos[0] = nextRow;
                        standardPos[1] = nextCol;

                        originalDir.addLast(originDir);
                        newDir.addFirst(newRotateDir);
                        pos[standardPos[0]][standardPos[1]] = true;
                    }
                }

                while (!originalDir.isEmpty()) {
                    int orginDir = originalDir.removeFirst();
                    newDir.addLast(orginDir);
                }
            }
        }

        int answer = checkSquare();
        System.out.println(answer);
    }
}