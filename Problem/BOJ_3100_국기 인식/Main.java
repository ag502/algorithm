import java.util.*;
import java.io.*;

public class Main {
    static int rows = 6;
    static int cols = 9;
    static String[][] flag = new String[rows][cols];
    static StringTokenizer st;

    static Map<String, Integer> partCount;
    static List<Map<String, Integer>> colors;

    public static int getChangeColorNum() {
        Map<String, Integer> middleColors = colors.get(1);
        int changedColorCount = Integer.MAX_VALUE;
        for (String middleColor : middleColors.keySet()) {
            int tempSum = 18 - middleColors.get(middleColor);
            for (int i = 0; i < colors.size(); i = i + 2) {
                Map<String, Integer> curColors = colors.get(i);
                int maxCount = Integer.MIN_VALUE;
                for (String curColor : curColors.keySet()) {
                    if (!curColor.equals(middleColor) && maxCount < curColors.get(curColor)) {
                        maxCount = curColors.get(curColor);
                    }
                    if (curColor.equals(middleColor)) {
                        continue;
                    }
                }
                if (maxCount == Integer.MIN_VALUE) {
                    tempSum = Integer.MAX_VALUE;
                    break;
                }
                tempSum += 18 - maxCount;
            }
            changedColorCount = Math.min(changedColorCount, tempSum);
        }
        return changedColorCount == Integer.MAX_VALUE ? 18 : changedColorCount;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_3100_국기 인식\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 국기 초기화
        for (int row = 0; row < rows; row++) {
            String[] oneRow = br.readLine().split("");
            for (int col = 0; col < cols; col++) {
                flag[row][col] = oneRow[col];
            }
        }

        // 가로 삼등분 확인
        int horizontalDivide = 0;
        colors = new ArrayList<>();
        for (int row = 0; row < rows; row = row + 2) {
            partCount = new HashMap<>();
            for (int i = row; i < row + 2; i++) {
                for (int j = 0; j < cols; j++) {
                    String curColor = flag[i][j];
                    int curCount = partCount.getOrDefault(curColor, 0);

                    partCount.put(curColor, curCount + 1);
                }
            }
            colors.add(partCount);
        }
        horizontalDivide = getChangeColorNum();

        // 세로 삼등분 확인
        int crossDivide = 0;
        colors = new ArrayList<>();
        for (int col = 0; col < cols; col = col + 3) {
            partCount = new HashMap<>();
            for (int i = 0; i < rows; i++) {
                for (int j = col; j < col + 3; j++) {
                    String curColor = flag[i][j];
                    int curCount = partCount.getOrDefault(curColor, 0);

                    partCount.put(curColor, curCount + 1);
                }
            }
            colors.add(partCount);
        }
        crossDivide = getChangeColorNum();
        System.out.println(Math.min(horizontalDivide, crossDivide));
    }
}
