import java.util.*;
import java.io.*;

public class Main {
    static int numOfStations, numOfLines, startStation, finishStation;
    // line: <station: [station]...>
    static Map<Integer, Map<Integer, Set<Integer>>> trainMap;
    // station: [line..]
    static Map<Integer, Set<Integer>> stationLines;
    static int[][] dist;

    static StringTokenizer st;

    public static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[numOfLines + 1][numOfStations + 1];
        dist = new int[numOfLines + 1][numOfStations + 1];

        for (int line = 1; line <= numOfLines; line++) {
            for (int station = 1; station <= numOfStations; station++) {
                dist[line][station] = Integer.MAX_VALUE;
            }
        }

        // 시작역이 포함된 노선 확인
        Set<Integer> startLines = stationLines.get(startStation);
        for (int line : startLines) {
            queue.add(new int[] { line, startStation });
            visited[line][startStation] = true;
            dist[line][startStation] = 0;
        }

        while (!queue.isEmpty()) {
            int[] curStationInfo = queue.poll();
            int curLine = curStationInfo[0];
            int curStation = curStationInfo[1];

            // 현재 노선의 역과 연결된 다음역 확인
            Set<Integer> nextStations = trainMap.get(curLine).get(curStation);
            for (int nextStation : nextStations) {
                Set<Integer> nextLines = stationLines.get(nextStation);
                for (int nextLine : nextLines) {
                    if (!visited[nextLine][nextStation]) {
                        visited[nextLine][nextStation] = true;
                        queue.add(new int[] { nextLine, nextStation });
                        if (curLine != nextLine) {
                            dist[nextLine][nextStation] = dist[curLine][curStation] + 1;
                        } else {
                            dist[nextLine][nextStation] = dist[curLine][curStation];
                        }
                    }
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2021_최소 환승 경로\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfStations = Integer.parseInt(st.nextToken());
        numOfLines = Integer.parseInt(st.nextToken());

        trainMap = new HashMap<>();
        stationLines = new HashMap<>();
        for (int line = 1; line <= numOfLines; line++) {
            trainMap.put(line, new HashMap<>());
            String[] stations = br.readLine().split(" ");
            for (int idx = 0; idx < stations.length - 2; idx++) {
                int curLine = line;
                int curStation = Integer.parseInt(stations[idx]);
                int nextStation = Integer.parseInt(stations[idx + 1]);

                // 라인별 노선
                trainMap.get(curLine).putIfAbsent(curStation, new HashSet<>());
                trainMap.get(curLine).putIfAbsent(nextStation, new HashSet<>());

                trainMap.get(curLine).computeIfPresent(curStation, (k, v) -> {
                    v.add(nextStation);
                    return v;
                });
                trainMap.get(curLine).computeIfPresent(nextStation, (k, v) -> {
                    v.add(curStation);
                    return v;
                });

                // 역별 라인
                stationLines.putIfAbsent(curStation, new HashSet<>());
                stationLines.putIfAbsent(nextStation, new HashSet<>());

                stationLines.computeIfPresent(curStation, (k, v) -> {
                    v.add(curLine);
                    return v;
                });
                stationLines.computeIfPresent(nextStation, (k, v) -> {
                    v.add(curLine);
                    return v;
                });
            }
        }

        // 출발역, 도착역 입력
        st = new StringTokenizer(br.readLine());
        startStation = Integer.parseInt(st.nextToken());
        finishStation = Integer.parseInt(st.nextToken());

        bfs();
        int answer = Integer.MAX_VALUE;
        for (int line = 1; line <= numOfLines; line++) {
            answer = Math.min(answer, dist[line][finishStation]);
        }

        System.out.println(answer);
    }
}