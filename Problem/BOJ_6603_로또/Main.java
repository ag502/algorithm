import java.io.*;
import java.util.*;

public class Main {
    static final int SELECTNUMBER = 6;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        visited = new boolean[50];

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int arraySize = Integer.parseInt(st.nextToken());

            if (arraySize == 0) {
                break;
            }

            int[] choosedArray = new int[arraySize + 1];
            for (int i = 1; i < arraySize + 1; i++) {
                choosedArray[i] = Integer.parseInt(st.nextToken());
            }

            for (int i = 1; i <= arraySize; i++) {
                selectLotto(i, 0, choosedArray, new ArrayList<String>());
            }

            System.out.println();
        }
    }

    public static void selectLotto(int curIdx, int selectedNum, int[] choosedArray, ArrayList<String> answer) {
        // 1. 방문
        visited[curIdx] = true;
        selectedNum++;
        // 2. 도착
        answer.add(Integer.toString(choosedArray[curIdx]));
        // 3. 갈 수 있는 숫자 순회
        for (int i = curIdx + 1; i < choosedArray.length; i++) {
            // 4. 갈 수 있는지 검사
            if (!visited[i] && selectedNum != SELECTNUMBER) {
                selectLotto(i, selectedNum, choosedArray, answer);
            }
        }
        // 4. 체크아웃
        if (answer.size() == SELECTNUMBER) {
            System.out.println(String.join(" ", answer));
        }
        answer.remove(answer.size() - 1);
        visited[curIdx] = false;
        selectedNum--;
    }
}