import java.util.*;
import java.io.*;

public class Main {
    static int numOfHouses, numOfRouters;
    static int[] housePositions;

    static StringTokenizer st;

    public static int getDistBetHouse() {
        int dist = 1000000001;
        int left = 0;
        int right = 1000000000;

        while (left <= right) {
            int curDist = (left + right) / 2;

            // 현재 거리 만큼 공유기 설치
            int curRouters = 1;
            int lastHouse = housePositions[0];
            for (int i = 1; i < numOfHouses; i++) {
                if (housePositions[i] - lastHouse < curDist) {
                    continue;
                }
                lastHouse = housePositions[i];
                curRouters++;
            }

            if (curRouters < numOfRouters) {
                right = curDist - 1;
            } else {
                left = curDist + 1;
                dist = curDist;
            }
        }

        return dist;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_2110_공유기 설치\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        st = new StringTokenizer(br.readLine());
        numOfHouses = Integer.parseInt(st.nextToken());
        numOfRouters = Integer.parseInt(st.nextToken());

        housePositions = new int[numOfHouses];
        for (int i = 0; i < numOfHouses; i++) {
            housePositions[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(housePositions);

        System.out.println(getDistBetHouse());
    }
}