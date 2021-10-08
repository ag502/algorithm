import java.util.*;
import java.io.*;

public class Main {
    static int numOfRivers;
    static int numOfRiverPaths;

    static Map<Integer, List<Integer>> riverRels;
    static int[] indegree;
    static int[] seq;
    static int[] count;

    static StringTokenizer st;

    public static void topologicalSort() {
        Queue<Integer> queue = new LinkedList<>();
        seq = new int[numOfRivers + 1];
        count = new int[numOfRivers + 1];

        for (int river = 1; river <= numOfRivers; river++) {
            if (indegree[river] == 0) {
                seq[river] += 1;
                queue.offer(river);
            }
        }

        while (!queue.isEmpty()) {
            int curRiver = queue.poll();

            for (int nextRiver : riverRels.get(curRiver)) {
                indegree[nextRiver]--;
                if (seq[nextRiver] < seq[curRiver]) {
                    seq[nextRiver] = seq[curRiver];
                    count[nextRiver] = 1;
                } else if (seq[nextRiver] == seq[curRiver]) {
                    count[nextRiver]++;
                }

                if (indegree[nextRiver] == 0) {
                    queue.offer(nextRiver);
                    if (count[nextRiver] >= 2) {
                        seq[nextRiver] += 1;
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_9470_Strahler 순서\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        int testCase = Integer.parseInt(br.readLine());
        for (int t = 0; t < testCase; t++) {
            st = new StringTokenizer(br.readLine());
            int curTestCase = Integer.parseInt(st.nextToken());
            numOfRivers = Integer.parseInt(st.nextToken());
            numOfRiverPaths = Integer.parseInt(st.nextToken());

            // graph 초기화
            riverRels = new HashMap<>();
            for (int river = 1; river <= numOfRivers; river++) {
                riverRels.put(river, new ArrayList<>());
            }

            // 강 경로 추가
            indegree = new int[numOfRivers + 1];
            for (int path = 0; path < numOfRiverPaths; path++) {
                st = new StringTokenizer(br.readLine());
                int startPoint = Integer.parseInt(st.nextToken());
                int endPoint = Integer.parseInt(st.nextToken());

                riverRels.computeIfPresent(startPoint, (k, v) -> {
                    v.add(endPoint);
                    indegree[endPoint]++;
                    return v;
                });
            }

            // topological sort
            topologicalSort();
            
            // answer
            System.out.println(curTestCase + " " + seq[numOfRivers]);
        }
    }
}