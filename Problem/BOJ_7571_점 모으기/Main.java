import java.util.*;
import java.io.*;

public class Main {
    static int squareSize;
    static int numOfPointer;

    static List<Integer> rowList;
    static List<Integer> colList;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_7571_점 모으기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        squareSize = Integer.parseInt(st.nextToken());
        numOfPointer = Integer.parseInt(st.nextToken());

        // 점 갯수 입력
        rowList = new ArrayList<>();
        colList = new ArrayList<>();
        for (int i = 0; i < numOfPointer; i++) {
            st = new StringTokenizer(br.readLine());
            int row = Integer.parseInt(st.nextToken());
            int col = Integer.parseInt(st.nextToken());

            rowList.add(row);
            colList.add(col);
        }

        // 오름차순 정렬
        Collections.sort(rowList);
        Collections.sort(colList);

        int rowMid = rowList.get(numOfPointer / 2);
        int colMid = colList.get(numOfPointer / 2);

        int answer = 0;
        for (int idx = 0; idx < rowList.size(); idx++) {
            answer += Math.abs(rowMid - rowList.get(idx));
        }

        for (int idx = 0; idx < colList.size(); idx++) {
            answer += Math.abs(colMid - colList.get(idx));
        }

        System.out.println(answer);
    }
}