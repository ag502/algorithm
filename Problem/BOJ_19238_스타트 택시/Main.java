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
        return this.row + " / " + this.col;
    }
}

class PriorityNode implements Comparable<PriorityNode> {
    int dist;
    int departRow, departCol, arrivalRow, arrivalCol, posIdx;

    public PriorityNode(int dist, int departRow, int departCol, int arrivalRow, int arrivalCol, int posIdx) {
        this.dist = dist;
        this.departRow = departRow;
        this.departCol = departCol;
        this.arrivalRow = arrivalRow;
        this.arrivalCol = arrivalCol;
        this.posIdx = posIdx;
    }

    @Override
    public int compareTo(PriorityNode p1) {
        if (this.dist == p1.dist) {
            if (this.departRow == p1.departRow) {
                return this.departCol - p1.departCol;
            }
            return this.departRow - p1.departRow;
        }
        return this.dist - p1.dist;
    }

    @Override
    public String toString() {
        return this.dist + " " + this.departRow + " " + this.departCol;
    }
}

class Main {
    static int[][] movingDir = { { -1, 0 }, { 0, 1 }, { 1, 0 }, { 0, -1 } };
    static int sizeOfWorld, numOfPassengers, fuel;
    static int[][] world;
    static Position taxiPosition;
    static Position[] departPositions;
    static Position[] arrivalPositions;
    static int[][] dist;

    static StringTokenizer st;

    public static void getMinDistToPassengers() {
        Queue<Position> queue = new LinkedList<>();
        boolean[][] visited = new boolean[sizeOfWorld + 1][sizeOfWorld + 1];

        // dist 초기화
        dist = new int[sizeOfWorld + 1][sizeOfWorld + 1];
        for (int row = 1; row <= sizeOfWorld; row++) {
            for (int col = 1; col <= sizeOfWorld; col++) {
                dist[row][col] = Integer.MAX_VALUE;
            }
        }
        queue.add(taxiPosition);
        visited[taxiPosition.row][taxiPosition.col] = true;
        dist[taxiPosition.row][taxiPosition.col] = 0;

        while (!queue.isEmpty()) {
            Position curPos = queue.poll();

            for (int i = 0; i < movingDir.length; i++) {
                int nextRow = curPos.row + movingDir[i][0];
                int nextCol = curPos.col + movingDir[i][1];

                if (1 <= nextRow && nextRow <= sizeOfWorld && 1 <= nextCol && nextCol <= sizeOfWorld) {
                    if (!visited[nextRow][nextCol] && world[nextRow][nextCol] == 0) {
                        queue.add(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                        dist[nextRow][nextCol] = dist[curPos.row][curPos.col] + 1;
                    }
                }
            }
        }
    }

    public static void getPassengerToArrival(int startRow, int startCol, int finishRow, int finishCol) {
        Queue<Position> queue = new LinkedList<>();
        boolean[][] visited = new boolean[sizeOfWorld + 1][sizeOfWorld + 1];

        // dist 초기화
        for (int row = 1; row <= sizeOfWorld; row++) {
            for (int col = 1; col <= sizeOfWorld; col++) {
                dist[row][col] = Integer.MAX_VALUE;
            }
        }
        dist[startRow][startCol] = 0;

        queue.add(new Position(startRow, startCol));
        visited[startRow][startCol] = true;

        while (!queue.isEmpty()) {
            Position curPos = queue.poll();

            if (curPos.row == finishRow && curPos.col == finishCol) {
                return;
            }

            for (int i = 0; i < movingDir.length; i++) {
                int nextRow = curPos.row + movingDir[i][0];
                int nextCol = curPos.col + movingDir[i][1];

                if (1 <= nextRow && nextRow <= sizeOfWorld && 1 <= nextCol && nextCol <= sizeOfWorld) {
                    if (!visited[nextRow][nextCol] && world[nextRow][nextCol] == 0) {
                        queue.add(new Position(nextRow, nextCol));
                        visited[nextRow][nextCol] = true;
                        dist[nextRow][nextCol] = dist[curPos.row][curPos.col] + 1;
                    }
                }
            }
        }
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

        // 현재 택시 위치 초기화
        st = new StringTokenizer(br.readLine());
        int curTaxiRow = Integer.parseInt(st.nextToken());
        int curTaxiCol = Integer.parseInt(st.nextToken());
        taxiPosition = new Position(curTaxiRow, curTaxiCol);

        // 출발지 도착지 위치 초기화
        departPositions = new Position[numOfPassengers + 1];
        arrivalPositions = new Position[numOfPassengers + 1];
        Set<Integer> positionList = new HashSet<>();

        for (int i = 1; i <= numOfPassengers; i++) {
            st = new StringTokenizer(br.readLine());
            int departRow = Integer.parseInt(st.nextToken());
            int departCol = Integer.parseInt(st.nextToken());
            int arrivalRow = Integer.parseInt(st.nextToken());
            int arrivalCol = Integer.parseInt(st.nextToken());

            departPositions[i] = new Position(departRow, departCol);
            arrivalPositions[i] = new Position(arrivalRow, arrivalCol);
            positionList.add(i);
        }

        int count = numOfPassengers;
        while (count > 0) {
            // 우선 순위 큐
            PriorityQueue<PriorityNode> pq = new PriorityQueue<>();
            // 택시에서 목적지까지 최단거리 계산
            getMinDistToPassengers();
            for (int posIdx : positionList) {
                Position curDepartPos = departPositions[posIdx];
                Position curArrivalPos = arrivalPositions[posIdx];
                int curDist = dist[curDepartPos.row][curDepartPos.col];
                pq.add(new PriorityNode(curDist, curDepartPos.row, curDepartPos.col, curArrivalPos.row,
                        curArrivalPos.col, posIdx));
            }

            PriorityNode curInfo = pq.poll();
            // 연료 부족으로 승객이 있는 곳으로 가지 못함
            if (fuel < curInfo.dist) {
                System.out.println(-1);
                return;
            }

            // 승객이 있는 곳으로 이동한 다면 연료 감소, 택시 위치 변경
            fuel -= curInfo.dist;
            taxiPosition.row = curInfo.departRow;
            taxiPosition.col = curInfo.departCol;

            // 출발지에서 목적지까지 최단 거리 계산
            getPassengerToArrival(curInfo.departRow, curInfo.departCol, curInfo.arrivalRow, curInfo.arrivalCol);

            // 연료 부족으로 목적지까지 가지 못함
            int curDist = dist[curInfo.arrivalRow][curInfo.arrivalCol];
            if (fuel < curDist) {
                System.out.println(-1);
                return;
            }

            // 목적지까지 이동할 수 있으면 연료 재지정 및 택시 위치 변경
            fuel = fuel - curDist + (curDist * 2);
            taxiPosition.row = curInfo.arrivalRow;
            taxiPosition.col = curInfo.arrivalCol;
            positionList.remove(curInfo.posIdx);
            count -= 1;
        }

        System.out.println(fuel);
    }
}