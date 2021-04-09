import java.util.*;
import java.io.*;

public class Main {
    static int numOfSnowball;
    static int[] snowballs;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        numOfSnowball = Integer.parseInt(br.readLine());
        snowballs = new int[numOfSnowball];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < snowballs.length; i++) {
            snowballs[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(snowballs);

        int answer = Integer.MAX_VALUE;
        for (int i = 0; i < numOfSnowball - 1; i++) {
            for (int j = i + 1; j < numOfSnowball; j++) {
                int snowMan1 = snowballs[i] + snowballs[j];
                int start = 0;
                int end = numOfSnowball - 1;

                while (start < end) {
                    if (start == i || start == j) {
                        start += 1;
                        continue;
                    }
                    if (end == i || end == j) {
                        end -= 1;
                        continue;
                    }

                    int snowMan2 = snowballs[start] + snowballs[end];
                    answer = Math.min(answer, Math.abs(snowMan1 - snowMan2));

                    if (snowMan1 > snowMan2) {
                        start += 1;
                    } else if (snowMan1 < snowMan2) {
                        end -= 1;
                    } else {
                        start += 1;
                        end -= 1;
                        System.out.println(answer);
                        return;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}
