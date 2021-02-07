import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    static int answer = 0;
    static int [] visited;
    static int lengthOfBoard;

    public static boolean isPossible(int nextRow, int nextCol) {
        for (int row = 0; row < nextRow; row++) {
            if (visited[row] == nextCol) {
                return false;
            }
            if (Math.abs(row - nextRow) == Math.abs(nextCol - visited[row])) {
                return false;
            }
        }
        return true;
    }

    public static void positioningQueen(int curQueen, int curRow, int curCol) {
        visited[curRow] = curCol;

        if (curQueen < lengthOfBoard) {
            for (int col = 0; col < lengthOfBoard; col++) {
                if (isPossible(curRow + 1, col)) {
                    positioningQueen(curQueen + 1, curRow + 1, col);
                }
            }
        }

        if (curQueen == lengthOfBoard) {
            answer += 1;
        }
        visited[curRow] = 0;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        lengthOfBoard = Integer.parseInt(br.readLine());
        visited = new int[lengthOfBoard];

        for (int col = 0; col < lengthOfBoard; col++) {
            positioningQueen(1, 0, col);
        }
        System.out.println(answer);
    }
}
