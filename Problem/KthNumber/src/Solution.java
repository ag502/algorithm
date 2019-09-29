import java.util.Arrays;

public class Solution {
    private static int[] splicing(int[] arr, int start, int end) {
        int[] newArray = new int[end - start + 1];
        for(int i = start - 1, j = 0; i < end; i++, j++) {
            newArray[j] = arr[i];
        }
        return newArray;
    }

    public int[] solution(int[] array, int[][] command) {
        int[] returnNumbers = new int[command.length];
        for(int i = 0; i < command.length; i++) {
            int startNum = command[i][0];
            int endNum = command[i][1];
            int kthNum = command[i][2];
            int[] splicedArray = splicing(array, startNum, endNum);
            Arrays.sort(splicedArray);
            returnNumbers[i] = splicedArray[kthNum - 1];
        }
        return returnNumbers;
    }

    public static void main(String[] args) {
        int[] test = {1, 5, 2, 6, 3, 7, 4};
        int[][] command = {{2, 5, 3}, {4, 4, 1}, {1, 7, 3}};
        System.out.println(Arrays.toString(new Solution().solution(test, command)));
    }
}
