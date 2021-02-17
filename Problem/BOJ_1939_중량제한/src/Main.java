import java.io.*;
import java.util.*;

public class Main {
    static int numOfIsland;
    static int numOfBridge;
    static int fIsland1;
    static int fIsland2;
    static Map<Integer, ArrayList<int []>> graph;
    static boolean[] visited;
    static StringTokenizer st;

    public static boolean dfs(int curIsland, int curWeight) {
        visited[curIsland] = true;

        ArrayList<int[]> curIslandInfo = graph.get(curIsland);
        for (int i = 0; i < curIslandInfo.size(); i++) {
            int nextIsland = curIslandInfo.get(i)[0];
            int nextWeight = curIslandInfo.get(i)[1];

            if (curIsland != fIsland2 && nextWeight >= curWeight && !visited[nextIsland]) {
                boolean answer = dfs(nextIsland, curWeight);
                if (answer) {
                    return true;
                } else {
                    continue;
                }
            }
        }
        if (curIsland == fIsland2) {
            return true;
        }
        return false;
    }

    public static int binarySearch() {
        int left = 1;
        int right = 1000000000;
        int answer = 0;

        while (left <= right) {
            visited = new boolean[numOfIsland + 1];
            int mid = (left + right) / 2;
            boolean go = dfs(fIsland1, mid);
            if (go) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        numOfIsland = Integer.parseInt(st.nextToken());
        numOfBridge = Integer.parseInt(st.nextToken());

        graph = new HashMap<>();

        for (int i = 0; i < numOfBridge; i++) {
            st = new StringTokenizer(br.readLine());
            int startIsland = Integer.parseInt(st.nextToken());
            int endIsland = Integer.parseInt(st.nextToken());
            int weightBridge = Integer.parseInt(st.nextToken());

            if (!graph.containsKey(startIsland)) {
                ArrayList<int []> array = new ArrayList<>();
                graph.put(startIsland, array);
            }
            if (!graph.containsKey(endIsland)) {
                ArrayList<int []> array = new ArrayList<>();
                graph.put(endIsland, array);
            }

            int[] info1 = {endIsland, weightBridge};
            graph.get(startIsland).add(info1);

            int[] info2 = {startIsland, weightBridge};
            graph.get(endIsland).add(info2);
        }

        st = new StringTokenizer(br.readLine());
        fIsland1 = Integer.parseInt(st.nextToken());
        fIsland2 = Integer.parseInt(st.nextToken());

        System.out.println(binarySearch());
    }
}
