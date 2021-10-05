import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    static int[] bottles = new int[4];
    static boolean[][][] visited = new boolean[201][201][201];

    static List<Integer> answer = new ArrayList<>();

    public static void bfs() {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] { 0, 0, bottles[3] });

        while (queue.size() != 0) {
            int[] curState = queue.poll();
            int firstBottle = curState[0];
            int secondBottle = curState[1];
            int thirdBottle = curState[2];

            if (visited[firstBottle][secondBottle][thirdBottle]) {
                continue;
            }

            visited[firstBottle][secondBottle][thirdBottle] = true;
            if (firstBottle == 0) {
                answer.add(thirdBottle);
            }

            // 1 -> 2
            if (firstBottle + secondBottle > bottles[2]) {
                queue.offer(new int[] { firstBottle + secondBottle - bottles[2], bottles[2], thirdBottle });
            } else {
                queue.offer(new int[] { 0, firstBottle + secondBottle, thirdBottle });
            }

            // 1 -> 3
            if (firstBottle + thirdBottle > bottles[3]) {
                queue.offer(new int[] { firstBottle + thirdBottle - bottles[3], secondBottle, bottles[3] });
            } else {
                queue.offer(new int[] { 0, secondBottle, firstBottle + thirdBottle });
            }

            // 2 -> 3
            if (secondBottle + thirdBottle > bottles[3]) {
                queue.offer(new int[] { firstBottle, secondBottle + thirdBottle - bottles[3], bottles[3] });
            } else {
                queue.offer(new int[] { firstBottle, 0, secondBottle + thirdBottle });
            }

            // 2 -> 1
            if (secondBottle + firstBottle > bottles[1]) {
                queue.offer(new int[] { bottles[1], secondBottle + firstBottle - bottles[1], thirdBottle });
            } else {
                queue.offer(new int[] { secondBottle + firstBottle, 0, thirdBottle });
            }

            // 3 -> 1
            if (thirdBottle + firstBottle > bottles[1]) {
                queue.offer(new int[] { bottles[1], secondBottle, thirdBottle + firstBottle - bottles[1] });
            } else {
                queue.offer(new int[] { thirdBottle + firstBottle, secondBottle, 0 });
            }

            // 3 -> 2
            if (thirdBottle + secondBottle > bottles[2]) {
                queue.offer(new int[] { firstBottle, bottles[2], thirdBottle + secondBottle - bottles[2] });
            } else {
                queue.offer(new int[] { firstBottle, secondBottle + thirdBottle, 0 });
            }
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2251_물통\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= 3; i++) {
            bottles[i] = Integer.parseInt(st.nextToken());
        }

        bfs();

        Collections.sort(answer, new Comparator<Integer>() {
            @Override
            public int compare(Integer o1, Integer o2) {
                return o1 - o2;
            }
        });

        System.out.println(answer.stream().map(v -> Integer.toString(v)).collect(Collectors.joining(" ")));
    }
}