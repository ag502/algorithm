import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    static int vertexs;
    static int edges;
    static int startVertex;

    static Map<Integer, List<Integer>> graph;
    static boolean[] visited;
    static List<Integer> answer;

    public static void dfs(int curVertex) {
        visited[curVertex] = true;
        answer.add(curVertex);

        List<Integer> nextVertexs = graph.get(curVertex);
        for (int i = 0; i < nextVertexs.size(); i++) {
            int nextVertex = nextVertexs.get(i);
            if (!visited[nextVertex]) {
                dfs(nextVertex);
            }
        }
    }

    public static void bfs(int curVertex) {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(curVertex);
        visited[curVertex] = true;

        while (queue.size() != 0) {
            int cur = queue.poll();
            answer.add(cur);

            List<Integer> nextVertexs = graph.get(cur);
            for (int i = 0; i < nextVertexs.size(); i++) {
                int nextVertex = nextVertexs.get(i);
                if (!visited[nextVertex]) {
                    queue.offer(nextVertex);
                    visited[nextVertex] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_1260_DFS와 BFS\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        vertexs = Integer.parseInt(st.nextToken());
        edges = Integer.parseInt(st.nextToken());
        startVertex = Integer.parseInt(st.nextToken());

        // graph 초기화
        graph = new HashMap<>();
        for (int vertex = 1; vertex <= vertexs; vertex++) {
            graph.put(vertex, new ArrayList<Integer>());
        }

        for (int edge = 1; edge <= edges; edge++) {
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

        // 인접 리스트 정렬
        for (int vertex = 1; vertex <= vertexs; vertex++) {
            graph.computeIfPresent(vertex, (k, v) -> {
                Collections.sort(v);
                return v;
            });
        }

        // dfs
        visited = new boolean[vertexs + 1];
        answer = new ArrayList<>();
        dfs(startVertex);

        System.out.println(answer.stream().map(v -> Integer.toString(v)).collect(Collectors.joining(" ")));

        // bfs
        visited = new boolean[vertexs + 1];
        answer.clear();
        bfs(startVertex);

        System.out.println(answer.stream().map(v -> Integer.toString(v)).collect(Collectors.joining(" ")));
    }
}