import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;

public class Solution {
    int [][] movingDir = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public int dfs(int[][] picture, boolean[][] visited, int targetColor, int curRow, int curCol, int count) {
        // 1. 방문
        visited[curRow][curCol] = true;
        // 2. 갈 수 있는 곳 탐방
        for (int i = 0; i < 4; i++) {
            int nextMovingRow = movingDir[i][0] + curRow;
            int nextMovingCol = movingDir[i][1] + curCol;

            if (0 <= nextMovingRow && nextMovingRow < picture.length && 0 <= nextMovingCol && nextMovingCol < picture[0].length) {
                if (!visited[nextMovingRow][nextMovingCol] && picture[nextMovingRow][nextMovingCol] == targetColor) {
                    // 3. 간다.
                    count = dfs(picture, visited, targetColor, nextMovingRow, nextMovingCol, count) + 1;
                }
            }
        }
        return count;
    }

    public int[] solution(int m, int n, int[][] picture) {
        int numberOfArea = 0;
        int maxSizeOfOneArea = 0;

        HashSet<Integer> colors = new HashSet<>();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] != 0) {
                    colors.add(picture[i][j]);
                }
            }
        }

        for (Integer color : colors) {
            boolean[][] visited = new boolean[m][n];
            for (int row = 0; row < m; row++) {
                for (int col = 0; col < n; col++) {
                    if (!visited[row][col] && picture[row][col] == color) {
                        numberOfArea += 1;
                        maxSizeOfOneArea = Math.max(maxSizeOfOneArea, dfs(picture, visited, color, row, col, 1));
                    }
                }
            }
        }

        int[] answer = new int[2];
        answer[0] = numberOfArea;
        answer[1] = maxSizeOfOneArea;
        return answer;
    }

    public static void main(String[] args) {
        int [][] picture = {{1, 1, 1, 0}, {1, 2, 2, 0}, {1, 0, 0, 1}, {0, 0, 0, 1}, {0, 0, 0, 3}, {0, 0, 0, 3}};
        Solution answer = new Solution();
        System.out.println(Arrays.toString(answer.solution(6, 4, picture)));
    }
}
