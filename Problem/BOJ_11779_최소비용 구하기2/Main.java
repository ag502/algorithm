import java.util.*;
import java.io.*;

public class Main {
    static int numOfCities;
    static int numOfBuses;
    static int startCity;
    static int targetCity;

    static Map<Integer, List<int[]>> busLines;
    static int[] dist;
    static int[] parent;

    static StringTokenizer st;

    public static void dijkstra() {
        // 기본 정보 초기화
        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o1[1] - o2[1];
            }
        });
        dist = new int[numOfCities + 1];
        parent = new int[numOfCities + 1];

        for (int i = 1; i <= numOfCities; i++) {
            dist[i] = Integer.MAX_VALUE;
        }

        pq.offer(new int[] { startCity, 0 });
        dist[startCity] = 0;
        parent[startCity] = startCity;

        // 다익스트라
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
                int nextCost = nextState[1];

                if (curDist + nextCost < dist[nextCity]) {
                    dist[nextCity] = curDist + nextCost;
                    pq.offer(new int[] { nextCity, dist[nextCity] });
                    parent[nextCity] = curCity;
                }
            }
        }
    }

    public static int findPath(Stack<Integer> path, int curCity) {
        int curParent = parent[curCity];
        path.push(curCity);
        if (curParent == curCity) {
            return curCity;
        }
        return findPath(path, curParent);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_11779_최소비용 구하기2\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfCities = Integer.parseInt(br.readLine());
        numOfBuses = Integer.parseInt(br.readLine());

        // 그래프 초기화
        busLines = new HashMap<>();
        for (int city = 1; city <= numOfCities; city++) {
            busLines.put(city, new ArrayList<>());
        }

        // 그래프 간선 추가
        for (int bus = 0; bus < numOfBuses; bus++) {
            st = new StringTokenizer(br.readLine());
            int startCity = Integer.parseInt(st.nextToken());
            int endCity = Integer.parseInt(st.nextToken());
            int cost = Integer.parseInt(st.nextToken());

            busLines.computeIfPresent(startCity, (k, v) -> {
                v.add(new int[] { endCity, cost });
                return v;
            });
        }

        // 시작, 도착 도시
        st = new StringTokenizer(br.readLine());
        startCity = Integer.parseInt(st.nextToken());
        targetCity = Integer.parseInt(st.nextToken());

        // 최단거리 구하기
        dijkstra();
        System.out.println(dist[targetCity]);

        Stack<Integer> path = new Stack<>();
        findPath(path, targetCity);

        System.out.println(path.size());

        StringBuilder sb = new StringBuilder("");
        while (path.size() != 0) {
            sb.append(path.pop());
            sb.append(" ");
        }

        System.out.println(sb.toString().trim());
    }
}