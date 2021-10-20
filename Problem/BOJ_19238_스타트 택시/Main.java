import java.util.*;
import java.io.*;

class Position {
    int row;
    int col;

    public Position(int row, int col) {
        this.row = row;
        this.col = col;
    }

    @Override
    public String toString() {
        return this.row + "/" + this.col;
    }
}

public class Main {
    static int[][] movingDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int sizeOfWorld, numOfPassengers, fuel;
    static int[][] world;
    static Position[] departPositions;
    static Position[] arrivePositions;
    static Position curTaxiPosition;
    static PriorityQueue<int[]> pq;
    static int minDist = Integer.MAX_VALUE;

    static StringTokenizer st;

    public static int getMinDist(int startRow, int startCol, int endRow, int endCol) {
        Deque<Position> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[sizeOfWorld + 1][sizeOfWorld + 1];

        queue.add(new Position(startRow, startCol));
        visited[startRow][startCol] = true;

        int dist = 0;
        while (!queue.isEmpty()) {
            int curSize = queue.size();

            dist += 1;
            for (int size = 0; size < curSize; size++) {
                Position curPos = queue.poll();

                if (dist > minDist) {
                    return Integer.MAX_VALUE;
                }

                if (curPos.row == endRow && curPos.col == endCol) {
                    return dist - 1;
                }

                for (int i = 0; i < movingDir.length; i++) {
                    int nextRow = curPos.row + movingDir[i][0];
                    int nextCol = curPos.col + movingDir[i][1];

                    if (1 <= nextRow && nextRow <= sizeOfWorld && 1 <= nextCol && nextCol <= sizeOfWorld) {
                        if (!visited[nextRow][nextCol] && world[nextRow][nextCol] == 0) {
                            visited[nextRow][nextCol] = true;
                            queue.add(new Position(nextRow, nextCol));
                        }
                    }
                }

            }

        }

        return Integer.MAX_VALUE;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_19238_스타트 택시\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        sizeOfWorld = Integer.parseInt(st.nextToken());
        numOfPassengers = Integer.parseInt(st.nextToken());
        fuel = Integer.parseInt(st.nextToken());

        // world 초기화
        world = new int[sizeOfWorld + 1][sizeOfWorld + 1];
        for (int row = 1; row <= sizeOfWorld; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 1; col <= sizeOfWorld; col++) {
                world[row][col] = Integer.parseInt(st.nextToken());
            }
        }

        // 초기 택시 위치 초기화
        st = new StringTokenizer(br.readLine());
        int curTaxiRow = Integer.parseInt(st.nextToken());
        int curTaxiCol = Integer.parseInt(st.nextToken());
        curTaxiPosition = new Position(curTaxiRow, curTaxiCol);

        // 승객 출발 탑승 위치, 완료 여부 배열 초기화
        Set<Integer> passengers = new HashSet<>();
        for (int i = 1; i <= numOfPassengers; i++) {
            passengers.add(i);
        }
        departPositions = new Position[numOfPassengers + 1];
        arrivePositions = new Position[numOfPassengers + 1];

        for (int i = 1; i <= numOfPassengers; i++) {
            st = new StringTokenizer(br.readLine());
            departPositions[i] = new Position(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
            arrivePositions[i] = new Position(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                if (o1[0] == o2[0]) {
                    if (o1[1] == o2[1]) {
                        return o1[2] - o2[2];
                    }
                    return o1[1] - o2[1];
                }
                return o1[0] - o2[0];
            }
        });
        int count = numOfPassengers;
        while (count > 0) {
            pq.clear();
            // 각각의 출발지에서 현재 택시 까지의 최소 거리
            for (int idx : passengers) {
                Position curDepartPos = departPositions[idx];
                int distToTaxi = getMinDist(curDepartPos.row, curDepartPos.col, curTaxiPosition.row,
                        curTaxiPosition.col);

                if (distToTaxi != Integer.MAX_VALUE) {
                    if (distToTaxi < minDist) {
                        minDist = distToTaxi;
                        pq.clear();
                        pq.add(new int[] { distToTaxi, departPositions[idx].row, departPositions[idx].col,
                                arrivePositions[idx].row, arrivePositions[idx].col, idx });
                    } else if (distToTaxi == minDist) {
                        pq.add(new int[] { distToTaxi, departPositions[idx].row, departPositions[idx].col,
                                arrivePositions[idx].row, arrivePositions[idx].col, idx });
                    }
                }

                // pq.add(new int[] { distToTaxi, departPositions[idx].row,
                // departPositions[idx].col,
                // arrivePositions[idx].row, arrivePositions[idx].col, idx });

            }

            // 탑승 위치
            int[] curDepartPos = pq.poll();
            System.out.println(Arrays.toString(curDepartPos));
            int distToTaxi = curDepartPos[0];
            int departRow = curDepartPos[1];
            int departCol = curDepartPos[2];

            // 연료가 부족하면 불가능
            if (fuel < distToTaxi || distToTaxi == Integer.MAX_VALUE) {
                System.out.println(-1);
                return;
            }
            // 탑승위치까지 택시이동
            fuel -= distToTaxi;
            curTaxiPosition.row = departRow;
            curTaxiPosition.col = departCol;

            // 탑승위치에서 도착지까지 이동
            int arriveRow = curDepartPos[3];
            int arriveCol = curDepartPos[4];
            minDist = Integer.MAX_VALUE;
            int dist = getMinDist(curTaxiPosition.row, curTaxiPosition.col, arriveRow, arriveCol);
            System.out.println(dist);
            // 가능 도중 연료가 부족하면 불가능
            if (fuel < dist || dist == Integer.MAX_VALUE) {
                System.out.println("a");

                System.out.println(-1);
                return;
            }
            // 도착
            fuel -= dist;
            fuel += dist * 2;
            curTaxiPosition.row = arriveRow;
            curTaxiPosition.col = arriveCol;
            passengers.remove(curDepartPos[5]);
            count -= 1;
        }

        System.out.println(fuel);
    }
}