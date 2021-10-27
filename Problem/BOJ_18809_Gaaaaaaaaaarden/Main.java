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
        return this.row + "," + this.col;
    }
}

public class Main {
    static int rows, cols, numOfGreen, numOfRed;
    static int[][] garden;
    static List<Position> yellowTilePos;
    static List<List<Position>> yellowTileCombList;
    static boolean[] visited;

    static StringTokenizer st;

    public static void getYellowTilePos(int curIdx, List<Position> temp) {
        temp.add(yellowTilePos.get(curIdx));
        visited[curIdx] = true;

        if (temp.size() < yellowTilePos.size()) {
            for (int nextIdx = 0; nextIdx < yellowTilePos.size(); nextIdx++) {
                if (!visited[nextIdx]) {
                    getYellowTilePos(nextIdx, temp);
                }
            }
        }

        if (temp.size() == yellowTilePos.size()) {
            List<Position> copy = new ArrayList<>();
            copy.addAll(temp);
            yellowTileCombList.add(copy);
        }

        temp.remove(temp.size() - 1);
        visited[curIdx] = false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_18809_Gaaaaaaaaaarden\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());
        numOfGreen = Integer.parseInt(st.nextToken());
        numOfRed = Integer.parseInt(st.nextToken());

        garden = new int[rows][cols];
        yellowTilePos = new ArrayList<>();

        for (int row = 0; row < rows; row++) {
            st = new StringTokenizer(br.readLine());
            for (int col = 0; col < cols; col++) {
                int curState = Integer.parseInt(st.nextToken());
                garden[row][col] = curState;
                if (curState == 1) {
                    yellowTilePos.add(new Position(row, col));
                }
            }
        }

        // 배양액 뿌릴 수 있는 타일 조구하기
        yellowTileCombList = new ArrayList<>();
        visited = new boolean[yellowTilePos.size()];
        for (int i = 0; i < yellowTilePos.size(); i++) {
            List<Position> temp = new ArrayList<>();
            getYellowTilePos(i, temp);
        }

        for (int i = 0; i < yellowTileCombList.size(); i++) {
            System.out.println(yellowTileCombList.get(i).toString());
        }
    }
}