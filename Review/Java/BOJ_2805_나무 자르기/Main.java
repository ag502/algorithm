import java.util.*;
import java.io.*;

public class Main {
    static int numOfTrees, targetTreeLength;
    static int trees[];

    static StringTokenizer st;

    public static int getCutterHeight() {
        int result = -1;
        int left = 0;
        int right = 1000000000;

        while (left <= right) {
            int cutterHeight = (left + right) / 2;
            // 설정한 높이로 잘랐을때 나무길이의 합
            long curHeightSum = 0;
            for (int curTreeHeight : trees) {
                if (curTreeHeight > cutterHeight) {
                    curHeightSum += curTreeHeight - cutterHeight;
                }
            }

            if (curHeightSum < targetTreeLength) {
                right = cutterHeight - 1;
            } else {
                left = cutterHeight + 1;
                result = cutterHeight;
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_2805_나무 자르기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfTrees = Integer.parseInt(st.nextToken());
        targetTreeLength = Integer.parseInt(st.nextToken());

        trees = new int[numOfTrees];
        st = new StringTokenizer(br.readLine());
        for (int tree = 0; tree < trees.length; tree++) {
            trees[tree] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(trees);

        System.out.println(getCutterHeight());
    }
}
