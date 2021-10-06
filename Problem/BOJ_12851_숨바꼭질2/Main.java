import java.util.*;
import java.io.*;

public class Main {
    static int startPos;
    static int finishPos;

    static boolean[] visited;
    static int dist = 0;
    static int answer = 0;

    public static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        visited = new boolean[100001];

        queue.offer(startPos);

        while (queue.size() != 0) {

            dist += 1;
            int curSize = queue.size();
            for (int size = 0; size < curSize; size++) {
                int curPos = queue.poll();
                visited[curPos] = true;

                if (curPos == finishPos) {
                    answer += 1;
                }

                int[] nextPos = { curPos - 1, curPos + 1, curPos * 2 };
                for (int pos : nextPos) {
                    if (0 <= pos && pos <= 100000 && !visited[pos]) {
                        queue.offer(pos);
                    }
                }
            }

            if (answer != 0) {
                break;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_12851_숨바꼭질2\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        startPos = Integer.parseInt(st.nextToken());
        finishPos = Integer.parseInt(st.nextToken());

        bfs();

        System.out.println(dist - 1);
        System.out.println(answer);
    }
}