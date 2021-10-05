import java.util.*;
import java.io.*;

public class Main {
    static int startPos;
    static int finishPos;

    static boolean[] visited;
    static int[] dist;

    public static void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        visited = new boolean[100001];
        dist = new int[100001];

        queue.offer(startPos);
        visited[startPos] = true;

        while (queue.size() != 0) {
            int curPos = queue.poll();

            if (curPos == finishPos) {
                break;
            }

            // 직선 이동
            if (0 <= curPos - 1 && curPos - 1 <= 100000 && !visited[curPos - 1]) {
                queue.offer(curPos - 1);
                visited[curPos - 1] = true;
                dist[curPos - 1] = dist[curPos] + 1;
            }

            if (0 <= curPos + 1 && curPos + 1 <= 100000 && !visited[curPos + 1]) {
                queue.offer(curPos + 1);
                visited[curPos + 1] = true;
                dist[curPos + 1] = dist[curPos] + 1;
            }

            // 순간 이동
            if (0 <= curPos * 2 && curPos * 2 <= 100000 && !visited[curPos * 2]) {
                queue.offer(curPos * 2);
                visited[curPos * 2] = true;
                dist[curPos * 2] = dist[curPos] + 1;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_1697_숨바꼭질\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        startPos = Integer.parseInt(st.nextToken());
        finishPos = Integer.parseInt(st.nextToken());

        bfs();

        System.out.println(dist[finishPos]);
    }
}