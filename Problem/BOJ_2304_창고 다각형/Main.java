import java.util.*;
import java.io.*;

class Pillar {
    int position;
    int height;

    public Pillar(int position, int height) {
        this.position = position;
        this.height = height;
    }

    @Override
    public String toString() {
        return this.position + "/" + this.height;
    }
}

public class Main {
    static int numOfPillars;
    static Map<Integer, Integer> pillars;
    static List<Integer> positionList;

    static StringTokenizer st;

    public static int getLeftMaxHeight(int boundIdx) {
        int maxHeight = Integer.MIN_VALUE;
        for (int idx = boundIdx - 1; idx >= 0; idx--) {
            maxHeight = Math.max(maxHeight, pillars.get(positionList.get(idx)));
        }
        return maxHeight;
    }

    public static int getRightMaxHeight(int boundIdx) {
        int maxHeight = Integer.MIN_VALUE;
        for (int idx = boundIdx + 1; idx < 1000; idx++) {
            maxHeight = Math.max(maxHeight, pillars.get(positionList.get(idx)));
        }
        return maxHeight;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2304_창고 다각형\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        pillars = new HashMap<>();
        for (int i = 1; i <= 1000; i++) {
            pillars.put(i, 0);
        }

        // input
        numOfPillars = Integer.parseInt(br.readLine());
        for (int i = 0; i < numOfPillars; i++) {
            st = new StringTokenizer(br.readLine());
            int position = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());

            pillars.computeIfPresent(position, (k, v) -> height);
        }

        positionList = new ArrayList<>(pillars.keySet());
        Collections.sort(positionList);

        int area = pillars.get(positionList.get(0)) + pillars.get(positionList.get(999));
        for (int i = 1; i < 999; i++) {
            int leftMaxHeight = getLeftMaxHeight(i);
            int rightMaxHeight = getRightMaxHeight(i);

            int minHeight = Math.min(leftMaxHeight, rightMaxHeight);
            if (pillars.get(positionList.get(i)) <= minHeight) {
                area += minHeight;
            } else {
                area += pillars.get(positionList.get(i));
            }
        }
        System.out.println(area);
    }
}