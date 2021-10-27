import java.util.*;
import java.io.*;

public class Main {
    static int numOfVideos, numOfQuestions;
    static Map<Integer, List<int[]>> graph;
    static int[] dist;
    static boolean[] visited;

    static StringTokenizer st;

    public static void bfs(int startVideo) {
        Queue<Integer> queue = new LinkedList<>();
        dist = new int[numOfVideos + 1];
        visited = new boolean[numOfVideos + 1];

        queue.add(startVideo);
        visited[startVideo] = true;
        dist[startVideo] = Integer.MAX_VALUE;

        while (!queue.isEmpty()) {
            int curVideo = queue.poll();

            List<int[]> nextVideoInfo = graph.get(curVideo);
            for (int[] nextInfo : nextVideoInfo) {
                int nextWeight = nextInfo[0];
                int nextVideo = nextInfo[1];

                if (!visited[nextVideo]) {
                    dist[nextVideo] = Math.min(dist[curVideo], nextWeight);
                    queue.add(nextVideo);
                    visited[nextVideo] = true;
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_15591_MooTube (Silver)\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfVideos = Integer.parseInt(st.nextToken());
        numOfQuestions = Integer.parseInt(st.nextToken());

        graph = new HashMap<>();
        for (int video = 1; video <= numOfVideos; video++) {
            graph.put(video, new ArrayList<int[]>());
        }

        for (int i = 0; i < numOfVideos - 1; i++) {
            st = new StringTokenizer(br.readLine());
            int startVideo = Integer.parseInt(st.nextToken());
            int finishVideo = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            graph.computeIfPresent(startVideo, (k, v) -> {
                v.add(new int[] { dist, finishVideo });
                return v;
            });

            graph.computeIfPresent(finishVideo, (k, v) -> {
                v.add(new int[] { dist, startVideo });
                return v;
            });
        }

        for (int q = 0; q < numOfQuestions; q++) {
            st = new StringTokenizer(br.readLine());
            int k = Integer.parseInt(st.nextToken());
            int startVideo = Integer.parseInt(st.nextToken());

            bfs(startVideo);

            int answer = 0;
            for (int video = 1; video <= numOfVideos; video++) {
                if (video != startVideo && k <= dist[video]) {
                    answer += 1;
                }
            }
            System.out.println(answer);
        }
    }
}