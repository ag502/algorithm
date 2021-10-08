import java.util.*;
import java.io.*;

public class Main {
    static int numOfBuildings;

    static Map<Integer, List<Integer>> buildingRels;
    static int[] indegree;
    static int[] times;
    static int[] dp;

    static StringTokenizer st;

    public static void topologicalSort() {
        Queue<Integer> queue = new LinkedList<>();
        dp = new int[numOfBuildings + 1];

        for (int building = 1; building <= numOfBuildings; building++) {
            if (indegree[building] == 0) {
                queue.offer(building);
                dp[building] = times[building];
            }
        }

        while (!queue.isEmpty()) {
            int curBuilding = queue.poll();

            for (int nextBuilding : buildingRels.get(curBuilding)) {
                indegree[nextBuilding]--;
                if (indegree[nextBuilding] == 0) {
                    queue.offer(nextBuilding);
                }
                dp[nextBuilding] = Math.max(dp[nextBuilding], dp[curBuilding] + times[nextBuilding]);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_1516_게임 개발\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfBuildings = Integer.parseInt(br.readLine());

        // 건물 관계 그래프 초기화
        buildingRels = new HashMap<>();
        for (int building = 1; building <= numOfBuildings; building++) {
            buildingRels.put(building, new ArrayList<>());
        }

        // 간선 추가
        indegree = new int[numOfBuildings + 1];
        times = new int[numOfBuildings + 1];

        for (int building = 1; building <= numOfBuildings; building++) {
            st = new StringTokenizer(br.readLine());
            int curTime = Integer.parseInt(st.nextToken());
            times[building] = curTime;

            while (true) {
                int curBuilding = building;
                int prevBuilding = Integer.parseInt(st.nextToken());
                if (prevBuilding == -1) {
                    break;
                }

                buildingRels.computeIfPresent(prevBuilding, (k, v) -> {
                    v.add(curBuilding);
                    indegree[curBuilding]++;
                    return v;
                });
            }
        }
        topologicalSort();

        for (int i = 1; i <= numOfBuildings; i++) {
            System.out.println(dp[i]);
        }
    }
}