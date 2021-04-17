import java.util.*;
import java.io.*;


public class Main {
    static int n;
    static int [][] movingDir = {{0, 1}, {1, 0}};
    static int[][] array;
    static int[][] dist;
    static StringTokenizer st;

    public static void dijkstra() {
        PriorityQueue<PositionInfo> pq = new PriorityQueue<>();
        pq.add(new PositionInfo(0, 1, 1));
        dist[1][1] = 0;

        while (pq.size() != 0) {
            PositionInfo curInfo = pq.poll();
            int curDist = curInfo.dist;
            int curRow = curInfo.row;
            int curCol = curInfo.col;

            if (curDist > dist[curRow][curCol]) {
                continue;
            }
            for (int i = 0; i < 2; i++) {
                int movingRow = movingDir[i][0];
                int movingCol = movingDir[i][1];
                int nextRow = curRow + movingRow;
                int nextCol = curCol + movingCol;
                if (1 <= nextRow && nextRow <= n && 1 <= nextCol && nextCol <= n) {
                    if (array[curRow][curCol] > array[nextRow][nextCol]) {
                        if (curDist < dist[nextRow][nextCol]) {
                            dist[nextRow][nextCol] = curDist;
                            pq.add(new PositionInfo(dist[nextRow][nextCol], nextRow, nextCol));
                        }
                    } else {
                        int count = array[nextRow][nextCol] - array[curRow][curCol] + 1;
                        if (curDist + count < dist[nextRow][nextCol]) {
                            dist[nextRow][nextCol] = curDist + count;
                            pq.add(new PositionInfo(dist[nextRow][nextCol], nextRow, nextCol));
                        }
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException{
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        n = Integer.parseInt(br.readLine());
        array = new int[n + 1][n + 1];
        dist = new int[n + 1][n + 1];

        for (int i = 1; i <= n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= n; j++) {
                array[i][j] = Integer.parseInt(st.nextToken());
                dist[i][j] = Integer.MAX_VALUE;
            }
        }

        dijkstra();
        System.out.println(dist[n][n]);

//        for (int i = 0; i <= n; i++) {
//            System.out.println(Arrays.toString(dist[i]));
//        }
    }
}

class PositionInfo implements Comparable<PositionInfo> {
    public int dist;
    public int row;
    public int col;

    PositionInfo(int dist, int row, int col) {
        this.dist = dist;
        this.row = row;
        this.col = col;
    }

    @Override
    public String toString() {
        return "PositionInfo{" +
                "dist=" + dist +
                ", row=" + row +
                ", col=" + col +
                '}';
    }

    @Override
    public int compareTo(PositionInfo positionInfo) {
        return this.dist - positionInfo.dist;
    }
}