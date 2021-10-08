import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    static int numOfWorks;

    static Map<Integer, List<Integer>> workRels;
    static Map<Integer, List<Integer>> parents;
    static int[] times;
    static int[] indegree;
    static int[] dp;

    static StringTokenizer st;

    public static void topologicalSort() {
        Queue<Integer> queue = new LinkedList<>();
        dp = new int[numOfWorks + 1];

        // indegree 0 인 정점 탐지
        for (int work = 1; work <= numOfWorks; work++) {
            if (indegree[work] == 0) {
                queue.offer(work);
                dp[work] = times[work];
            }
        }

        // queue 순회
        while (!queue.isEmpty()) {
            int curWork = queue.poll();

            int maxTime = 0;
            for (int curParent : parents.get(curWork)) {
                maxTime = Math.max(maxTime, dp[curParent]);
            }
            dp[curWork] = maxTime + times[curWork];

            for (int nextWork : workRels.get(curWork)) {
                indegree[nextWork]--;
                if (indegree[nextWork] == 0) {
                    queue.offer(nextWork);
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2056_작업\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfWorks = Integer.parseInt(br.readLine());

        // 작업 그래프 초기화
        workRels = new HashMap<>();
        parents = new HashMap<>();

        for (int work = 1; work <= numOfWorks; work++) {
            workRels.put(work, new ArrayList<>());
            parents.put(work, new ArrayList<>());
        }

        // 작업 그래프 간선 추가
        indegree = new int[numOfWorks + 1];
        times = new int[numOfWorks + 1];

        for (int curWork = 1; curWork <= numOfWorks; curWork++) {
            st = new StringTokenizer(br.readLine());
            int time = Integer.parseInt(st.nextToken());
            int numOfPrevWork = Integer.parseInt(st.nextToken());

            times[curWork] = time;

            // 선행 작업 입력
            for (int j = 0; j < numOfPrevWork; j++) {
                int prevWork = Integer.parseInt(st.nextToken());
                int curWorkTemp = curWork;

                indegree[curWork]++;
                workRels.computeIfPresent(prevWork, (k, v) -> {
                    v.add(curWorkTemp);
                    return v;
                });

                parents.computeIfPresent(curWork, (k, v) -> {
                    v.add(prevWork);
                    return v;
                });
            }
        }

        // 위상 정렬
        topologicalSort();

        System.out.println(Arrays.stream(dp).max().getAsInt());
    }
}