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
        return this.row + " / " + this.col;
    }
}

public class Main {
    static int[][] movingDir = { { 0, -1 }, { 0, 1 }, { -1, 0 }, { 1, 0 } };
    static int rows, cols;
    static char[][] board;
    static Deque<Integer> dirComb;
    static Position firstCoin;
    static Position secondCoin;

    public static void movingCoin(int targetCount) {
        Position newFirsPosition = new Position(firstCoin.row, firstCoin.col);
        Position newSecondPosition = new Position(secondCoin.row, secondCoin.col);

        for (int curDir : dirComb) {
            // 첫번째 동전
            boolean isFirstOut = false;
            boolean isSecondOut = false;
            int firstCNextRow = newFirsPosition.row + movingDir[curDir][0];
            int firstCNextCol = newFirsPosition.col + movingDir[curDir][1];

            if (0 > firstCNextRow || rows <= firstCNextRow || 0 > firstCNextCol || cols <= firstCNextCol) {
                isFirstOut = true;
            } else {
                if (board[firstCNextRow][firstCNextCol] != '#') {
                    newFirsPosition.row = firstCNextRow;
                    newFirsPosition.col = firstCNextCol;
                }
            }

            // 두번째 동전
            int secondCNextRow = newSecondPosition.row + movingDir[curDir][0];
            int secondCNextCol = newSecondPosition.col + movingDir[curDir][1];

            if (0 > secondCNextRow || rows <= secondCNextRow || 0 > secondCNextCol || cols <= secondCNextCol) {
                isSecondOut = true;
            } else {
                if (board[secondCNextRow][secondCNextCol] != '#') {
                    newSecondPosition.row = secondCNextRow;
                    newSecondPosition.col = secondCNextCol;
                }
            }

            if (isFirstOut && isSecondOut) {
                return;
            } else if (isFirstOut || isSecondOut) {
                System.out.println(targetCount);
                System.exit(0);
            }
        }
    }

    public static void getDirCombinations(int curDir, int curCount, int targetCount) {
        dirComb.add(curDir);

        if (curCount < targetCount) {
            for (int nextDir = 0; nextDir < 4; nextDir++) {
                getDirCombinations(nextDir, curCount + 1, targetCount);
            }
        }

        if (curCount == targetCount) {
            movingCoin(targetCount);
        }
        dirComb.pollLast();
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_16197_두 동전\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        rows = Integer.parseInt(st.nextToken());
        cols = Integer.parseInt(st.nextToken());

        board = new char[rows][cols];
        boolean isFirst = true;
        for (int row = 0; row < rows; row++) {
            board[row] = br.readLine().toCharArray();
            for (int col = 0; col < cols; col++) {
                if (board[row][col] == 'o') {
                    if (isFirst) {
                        firstCoin = new Position(row, col);
                        isFirst = false;
                    } else {
                        secondCoin = new Position(row, col);
                    }
                }
            }
        }

        dirComb = new ArrayDeque<>();
        for (int count = 1; count <= 10; count++) {
            for (int startDir = 0; startDir < 4; startDir++) {
                getDirCombinations(startDir, 1, count);
            }
        }

        System.out.println(-1);
    }
}