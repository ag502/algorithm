import java.util.*;
import java.io.*;

public class Main {
    static int numOfLiquids;
    static int[] liquids;

    // 이하인 값 중 최댓값
    public static int binarySearch(int left, int right, int targetValue) {
        int res = left - 1;

        while (left <= right) {
            int midIdx = (left + right) / 2;
            if (liquids[midIdx] <= targetValue) {
                left = midIdx + 1;
                res = midIdx;
            } else {
                right = midIdx - 1;
            }
        }

        return res;

    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_2470_두 용액\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfLiquids = Integer.parseInt(br.readLine());
        liquids = new int[numOfLiquids];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < numOfLiquids; i++) {
            liquids[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(liquids);

        int bestSum = Integer.MAX_VALUE;
        int[] answer = new int[2];
        for (int left = 0; left < liquids.length - 1; left++) {
            int findIdx = binarySearch(left + 1, liquids.length - 1, -liquids[left]);

            if (findIdx >= left + 1 && bestSum > Math.abs(liquids[left] + liquids[findIdx])) {
                bestSum = Math.abs(liquids[left] + liquids[findIdx]);
                answer[0] = liquids[left];
                answer[1] = liquids[findIdx];
            }
            // if (findIdx - 1 >= left + 1 && bestSum > Math.abs(liquids[left] + liquids[findIdx - 1])) {
            //     bestSum = Math.abs(liquids[left] + liquids[findIdx - 1]);
            //     answer[0] = liquids[left];
            //     answer[1] = liquids[findIdx - 1];
            // }
            if (findIdx + 1 >= left + 1 && findIdx + 1 < liquids.length
                    && bestSum > Math.abs(liquids[left] + liquids[findIdx + 1])) {
                bestSum = Math.abs(liquids[left] + liquids[findIdx + 1]);
                answer[0] = liquids[left];
                answer[1] = liquids[findIdx + 1];
            }
        }
        System.out.println(answer[0] + " " + answer[1]);
    }
}