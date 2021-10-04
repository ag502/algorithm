import java.util.*;
import java.io.*;

public class Main {
    static int numOfVertexes;
    static int numOfEdges;

    static Map<Integer, List<Integer>> graph;
    static boolean visited[];
    static StringTokenizer st;

    public static void dfs(int curVertex) {
        visited[curVertex] = true;

        List<Integer> nextVertexes = graph.get(curVertex);
        for (int i = 0; i < nextVertexes.size(); i++) {
            int nextVertex = nextVertexes.get(i);
            if (!visited[nextVertex]) {
                dfs(nextVertex);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_11724_연결 요소의 개수\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfVertexes = Integer.parseInt(st.nextToken());
        numOfEdges = Integer.parseInt(st.nextToken());

        // graph 초기화
        graph = new HashMap<>();
        for (int vertex = 1; vertex <= numOfVertexes; vertex++) {
            graph.put(vertex, new ArrayList<Integer>());
        }

        for (int edge = 0; edge < numOfEdges; edge++) {
            st = new StringTokenizer(br.readLine());
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());

            graph.computeIfPresent(from, (k, v) -> {
                v.add(to);
                return v;
            });

            graph.computeIfPresent(to, (k, v) -> {
                v.add(from);
                return v;
            });
        }

        int numOfConnection = 0;
        visited = new boolean[numOfVertexes + 1];
        for (int vertex = 1; vertex <= numOfVertexes; vertex++) {
            if (!visited[vertex]) {
                numOfConnection += 1;
                dfs(vertex);
            }
        }

        System.out.println(numOfConnection);
    }
}