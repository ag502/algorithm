import java.util.Arrays;

public class Solution {
    private void swap(String[] array, int idx1, int idx2) {
        String temp = array[idx1];
        array[idx1] = array[idx2];
        array[idx2] = temp;
    }

    private int isDictionaryOrder(String s1, String s2) {
        return s1.compareTo(s2);
    }
    private int partition(String[] array, int start, int end, int n) {
        int index = start, bigNum = start;
        int pivot = end;
        while(index < end) {
            if (array[pivot].charAt(n) == array[index].charAt(n)) {
                int compareResult = isDictionaryOrder(array[pivot], array[index]);
                if (compareResult >= 0) {
                    swap(array, index, bigNum);
                    bigNum++;
                }
            } else if(array[pivot].charAt(n) > array[index].charAt(n)) {
                swap(array, index, bigNum);
                bigNum++;
            }
            index++;
        }
        swap(array, pivot, bigNum);
        pivot = bigNum;
        return pivot;
    }

    private void quickStringSort(String[] strings, int start, int end, int n) {
        if (end - start < 0) {
            return;
        }
        int pivot = partition(strings, start, end, n);
        quickStringSort(strings, start, pivot - 1, n);
        quickStringSort(strings, pivot + 1, end, n);
    }

    public String[] solution(String[] strings, int n) {
        quickStringSort(strings, 0, strings.length - 1, n);
        return strings;
    }

    public static void main(String[] args) {
        String[] test1 = {"sun", "bed", "car"};
        String[] test2 = {"abcd", "abce", "cdx"};
        String[] test3 = {"abfd", "abcd", "abad", "abcx", "abcd"};
        String[] test4 = {"abfd", "abcd", "abad", "abcx"};

        new Solution().solution(test1, 1);
        System.out.println(Arrays.toString(new Solution().solution(test1, 1)));
//        new Solution().solution(test2, 0, test2.length - 1, 1);
//        System.out.println(Arrays.toString(test2));
//        new Solution().solution(test3, 0, test3.length - 1, 1);
//        System.out.println(Arrays.toString(test3));
    }
}
