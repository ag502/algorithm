import java.util.*;
import java.io.*;

public class Main {
    static int inspectionTime;
    static HashMap<Integer, Integer> cowInfo = new HashMap<>();
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int answer = 0;
        inspectionTime = Integer.parseInt(br.readLine());
        for (int i = 0; i < inspectionTime; i++) {
            st = new StringTokenizer(br.readLine());
            int cow = Integer.parseInt(st.nextToken());
            int dir = Integer.parseInt(st.nextToken());
            if (cowInfo.containsKey(cow)) {
                if (cowInfo.get(cow) != dir) {
                    answer += 1;
                    cowInfo.replace(cow, dir);
                }
            } else {
                cowInfo.put(cow, dir);
            }
        }
        System.out.println(answer);
    }
}
