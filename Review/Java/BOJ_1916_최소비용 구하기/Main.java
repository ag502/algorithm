import java.util.*;
import java.io.*;

public class Main {
    static int numOfCities;
    static int numOfBuses;

    static Map<Integer, List<int[]>> busLines;
    static int startCity;
    static int endCity;

    static int[] dist;
    static StringTokenizer st;

    public static void dijkstra() {
        // 우선 순위 큐, dist 초기화
        dist = new int[numOfCities + 1];
        for (int city = 1; city <= numOfCities; city++) {
            dist[city] = Integer.MAX_VALUE;
        }
        dist[startCity] = 0;

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        pq.offer(new int[] { startCity, 0 });

        // dijkstra
        while (pq.size() != 0) {
            int[] curState = pq.poll();
            int curCity = curState[0];
            int curDist = curState[1];

            if (dist[curCity] < curDist) {
                continue;
            }

            List<int[]> nextCities = busLines.get(curCity);
            for (int idx = 0; idx < nextCities.size(); idx++) {
                int[] nextState = nextCities.get(idx);
                int nextCity = nextState[0];
                int nextDist = nextState[1];

                if (curDist + nextDist < dist[nextCity]) {
                    dist[nextCity] = curDist + nextDist;
                    pq.offer(new int[] { nextCity, dist[nextCity] });
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_1916_최소비용 구하기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfCities = Integer.parseInt(br.readLine());
        numOfBuses = Integer.parseInt(br.readLine());

        // busline 초기화
        busLines = new HashMap<>();
        for (int city = 1; city <= numOfCities; city++) {
            busLines.put(city, new ArrayList<>());
        }

        for (int bus = 0; bus < numOfBuses; bus++) {
            st = new StringTokenizer(br.readLine());
            int startCity = Integer.parseInt(st.nextToken());
            int endCity = Integer.parseInt(st.nextToken());
            int weight = Integer.parseInt(st.nextToken());

            busLines.computeIfPresent(startCity, (k, v) -> {
                v.add(new int[] { endCity, weight });
                return v;
            });
        }

        // 출발 도착 도시
        st = new StringTokenizer(br.readLine());
        startCity = Integer.parseInt(st.nextToken());
        endCity = Integer.parseInt(st.nextToken());

        dijkstra();

        System.out.println(dist[endCity]);
    }
}