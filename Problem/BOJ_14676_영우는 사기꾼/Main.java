import java.util.*;
import java.io.*;

public class Main {
    static int numOfBuildings;
    static int numOfRels;
    static int numOfInfo;

    static Map<Integer, List<Integer>> buildingRels;
    static int[] indegree;
    static int[] isConstructor;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14676_영우는 사기꾼\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfBuildings = Integer.parseInt(st.nextToken());
        numOfRels = Integer.parseInt(st.nextToken());
        numOfInfo = Integer.parseInt(st.nextToken());

        // 빌딩 순서 그래프 초기화
        buildingRels = new HashMap<>();
        for (int building = 1; building <= numOfBuildings; building++) {
            buildingRels.put(building, new ArrayList<>());
        }

        // 간선 추가
        indegree = new int[numOfBuildings + 1];
        isConstructor = new int[numOfBuildings + 1];
        for (int rel = 0; rel < numOfRels; rel++) {
            st = new StringTokenizer(br.readLine());
            int prevBuilding = Integer.parseInt(st.nextToken());
            int nextBuilding = Integer.parseInt(st.nextToken());

            buildingRels.computeIfPresent(prevBuilding, (k, v) -> {
                v.add(nextBuilding);
                indegree[nextBuilding]++;
                return v;
            });
        }

        for (int info = 0; info < numOfInfo; info++) {
            st = new StringTokenizer(br.readLine());
            int state = Integer.parseInt(st.nextToken());
            int building = Integer.parseInt(st.nextToken());

            if (state == 1) {
                if (indegree[building] <= 0) {
                    isConstructor[building]++;
                    for (int nextBuilding : buildingRels.get(building)) {
                        indegree[nextBuilding]--;
                    }
                } else {
                    System.out.println("Lier!");
                    return;
                }
            } else if (state == 2) {
                if (isConstructor[building] > 0) {
                    isConstructor[building]--;
                    for (int nextBuilding : buildingRels.get(building)) {
                        indegree[nextBuilding]++;
                    }
                } else {
                    System.out.println("Lier!");
                    return;
                }
            }
        }
        System.out.println("King-God-Emperor");
    }
}
