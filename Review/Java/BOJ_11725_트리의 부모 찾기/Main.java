import java.util.*;
import java.io.*;

public class Main {
    static int numOfNodes;

    static Map<Integer, List<Integer>> tree;
    static boolean[] visited;
    static int[] parents;

    public static void dfs(int curNode) {
        visited[curNode] = true;

        List<Integer> nextNodes = tree.get(curNode);
        for (int idx = 0; idx < nextNodes.size(); idx++) {
            int nextNode = nextNodes.get(idx);
            if (!visited[nextNode]) {
                parents[nextNode] = curNode;
                dfs(nextNode);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_11725_트리의 부모 찾기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        numOfNodes = Integer.parseInt(st.nextToken());

        // tree 초기화
        tree = new HashMap<>();
        for (int node = 1; node <= numOfNodes; node++) {
            tree.put(node, new ArrayList<Integer>());
        }

        for (int i = 0; i < numOfNodes - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int parent = Integer.parseInt(st.nextToken());
            int child = Integer.parseInt(st.nextToken());

            tree.computeIfPresent(parent, (k, v) -> {
                v.add(child);
                return v;
            });

            tree.computeIfPresent(child, (k, v) -> {
                v.add(parent);
                return v;
            });
        }

        // dfs
        visited = new boolean[numOfNodes + 1];
        parents = new int[numOfNodes + 1];
        dfs(1);

        for (int node = 2; node <= numOfNodes; node++) {
            System.out.println(parents[node]);
        }
    }
}