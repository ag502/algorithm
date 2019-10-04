import java.util.*;

class Student {
    private int[] pattern;
    private int correctNum;

    Student(int[] pattern) {
        this.pattern = pattern;
        correctNum = 0;
    }

    public int compareTwoArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            int j = i;
            if (j >= this.pattern.length) {
                j = i % this.pattern.length;
            }
            if (array[i] == this.pattern[j]) {
                correctNum++;
            }
        }
        return correctNum;
    }

    public int getCorrectNum() {
        return this.correctNum;
    }
}

public class Solution {
    private final int[] STUDENT_A_PATTERN = { 1, 2, 3, 4, 5 };
    private final int[] STUDENT_B_PATTERN = { 2, 1, 2, 3, 2, 4, 2, 5 };
    private final int[] STUDENT_C_PATTERN = { 3, 3, 1, 1, 2, 2, 4, 4, 5, 5 };


//    private int compareTwoArray(int[] array, int[] table) {
//        int numOfSame = 0;
//        for (int i = 0; i < array.length; i++) {
//            int j = i;
//            if (j >= table.length) {
//                j = i % table.length;
//            }
//            if (array[i] == table[j]) {
//                numOfSame++;
//            }
//        }
//        return numOfSame;
//    }

    public int[] solution(int[] answers) {
        Student stuA = new Student(STUDENT_A_PATTERN);
        Student stuB = new Student(STUDENT_B_PATTERN);
        Student stuC = new Student(STUDENT_C_PATTERN);

        stuA.compareTwoArray(answers);
        stuB.compareTwoArray(answers);
        stuC.compareTwoArray(answers);

        int[] correctNumbers = {stuA.getCorrectNum(), stuB.getCorrectNum(), stuC.getCorrectNum()};

        int max = correctNumbers[0];
        int numOfMax = 1;

        for (int i = 1; i < correctNumbers.length; i++) {
            if (max < correctNumbers[i]) {
                max = correctNumbers[i];
                numOfMax = 1;
            } else if (max == correctNumbers[i]) {
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
        int[] a2 = {1, 3, 2, 4, 2};
        System.out.println(Arrays.toString(new Solution().solution(a1)));
        System.out.println(Arrays.toString(new Solution().solution(a2)));
    }
}

