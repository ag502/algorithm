import java.util.*;

public class Solution {
    private final int[] STUDENT_A = { 1, 2, 3, 4, 5 };
    private final int[] STUDENT_B = { 2, 1, 2, 3, 2, 4, 2, 5 };
    private final int[] STUDENT_C = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };

    private int compareTwoArray(int[] array, int[] table) {
        int numOfSame = 0;
        for (int i = 0; i < array.length; i++) {
            int j = i;
            if (j >= table.length) {
                j = i % table.length;
            }
            if (array[i] == table[j]) {
                numOfSame++;
            }
        }
        return numOfSame;
    }

    public int[] solution(int[] answers) {
        int[][] students = { STUDENT_A, STUDENT_B, STUDENT_C };
        int[] correctNumbers = new int[3];

        int correctNum = compareTwoArray(answers, students[0]);
        correctNumbers[0] = correctNum;

        int max = correctNum;
        int numOfMax = 0;

        for (int i = 1; i < students.length; i++) {
            correctNum = compareTwoArray(answers, students[i]);
            correctNumbers[i] = correctNum;
            if (max < correctNum) {
                max = correctNum;
                numOfMax = 1;
            } else if (max == correctNum) {
                numOfMax++;
            }
        }
        int[] maxCorrectStudent = new int[numOfMax];
        int index = 0;
        for (int i = 0; i < correctNumbers.length; i++) {
            if (correctNumbers[i] == max) {
                maxCorrectStudent[index++] = i + 1;
            }
        }
        return maxCorrectStudent;
    }

    public static void main(String[] args) {
        int[] a1 = {1, 2, 3, 4, 5};
        int[] a2 = {3, 2, 4, 2, 1, 3, 2, 4, 2, 1, 3, 2, 4, 2, 1, 3, 2};
        System.out.println(Arrays.toString(new Solution().solution(a1)));
        System.out.println(Arrays.toString(new Solution().solution(a2)));
    }
}

