import java.util.*;
import java.io.*;

public class Main {
    static String[] fence;
    static double[] fenceCost;

    // 0 ~ fenceIdx까지 최소 수리비용
    public static double fixFence(int fenceIdx) {
        if (fenceIdx < 0) {
            return 0;
        } else if (fenceCost[fenceIdx] != Double.MAX_VALUE) {
            return fenceCost[fenceIdx];
        } else if (fenceIdx == 1) {
            return 1;
        }

        double cost = Math.sqrt(fenceIdx + 1);

        if (fence[fenceIdx].equals(".")) {
            cost = fenceCost[fenceIdx - 1];
        } else {
            for (int i = 0; i <= fenceIdx; i++) {
                double newCost = 0;
                newCost += Math.sqrt(fenceIdx - i + 1);
                newCost += fixFence(fenceIdx - 1);
                if (cost > newCost) {
                    cost = newCost;
                }
            }
        }
        fenceCost[fenceIdx] = cost;
        return fenceCost[fenceIdx];
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\grm_10B\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 펜스 입력 받기
        fence = br.readLine().split("");

        fenceCost = new double[fence.length];
        for (int i = 0; i < fenceCost.length; i++) {
            fenceCost[i] = Double.MAX_VALUE;
        }

        for (int i = 0; i < fence.length; i++) {
            fixFence(i);
        }
        System.out.println(String.format("%.3f", fenceCost[fenceCost.length - 1]));
    }
}