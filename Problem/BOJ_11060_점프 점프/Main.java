import java.util.*;
import java.io.*;

// bfs
// public class Main {
//     public static void main(String[] args) throws IOException {
//         System.setIn(new FileInputStream("Problem\\BOJ_11060_점프 점프\\input.txt"));
//         BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

//         // input
//         StringTokenizer st = new StringTokenizer(br.readLine());
//         int cells = Integer.parseInt(st.nextToken());

//         int[] maze = new int[cells];
//         st = new StringTokenizer(br.readLine());
//         for (int col = 0; col < cells; col++) {
//             maze[col] = Integer.parseInt(st.nextToken());
//         }

//         // graph 생성 및 초기화
//         Map<Integer, List<Integer>> graph = new HashMap<>();
//         for (int node = 0; node < cells; node++) {
//             graph.put(node, new ArrayList<>());
//         }

//         for (int node = 0; node < cells; node++) {
//             for (int dist = 1; dist < maze[node] + 1; dist++) {
//                 if (node + dist < cells) {
//                     List<Integer> curList = graph.get(node);
//                     curList.add(node + dist);
//                 }
//             }
//         }

//         // for (int i = 0; i < graph.size(); i++) {
//         //     System.out.println(graph.get(i).toString());
//         // }

//         Queue<Integer> queue = new LinkedList<>();
//         boolean[] visited = new boolean[cells];
//         queue.offer(0);
//         visited[0] = true;

//         int time = 0;
//         while (queue.size() != 0) {
//             time++;
//             int curSize = queue.size();
//             for (int i = 0; i < curSize; i++) {
//                 int curNode = queue.poll();
//                 if (curNode == cells - 1) {
//                     System.out.println(time - 1);
//                     return;
//                 }
//                 for (int j = 0; j < graph.get(curNode).size(); j++) {
//                     int nextNode = graph.get(curNode).get(j);
//                     if (!visited[nextNode]) {
//                         queue.offer(nextNode);
//                         visited[nextNode] = true;
//                     }
//                 }
//             }
//         }
//         System.out.println(-1);
//     }
// }

// dp

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_11060_점프 점프\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        int numOfCells = Integer.parseInt(st.nextToken());

        int[] maze = new int[numOfCells];
        st = new StringTokenizer(br.readLine());
        for (int col = 0; col < numOfCells; col++) {
            maze[col] = Integer.parseInt(st.nextToken());
        }

        // dp
        int[] dp = new int[numOfCells];
        // dp 배열 초기화
        for (int i = 0; i < numOfCells; i++) {
            dp[i] = Integer.MAX_VALUE;
        }
        dp[0] = 0;

        for (int i = 0; i < numOfCells; i++) {
            if (dp[i] == Integer.MAX_VALUE) {
                continue;
            }
            int curStep = maze[i];
            for (int step = 1; step <= curStep; step++) {
                if (i + step < numOfCells) {
                    dp[i + step] = Math.min(dp[i + step], dp[i] + 1);
                }
            }
        }
        // System.out.println(Arrays.toString(dp));
        System.out.println(dp[numOfCells - 1] == Integer.MAX_VALUE ? -1 : dp[numOfCells - 1]);
    }
}