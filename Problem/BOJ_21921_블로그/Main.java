import java.util.*;
import java.util.stream.Collectors;
import java.io.*;

public class Main {
    static int days;
    static int windowSize;
    static StringTokenizer st;
    static int maxVisitors = Integer.MIN_VALUE;

    static int sumOfVisitors = 0;
    static int count = 0;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_21921_블로그\\input.txt"));

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        days = Integer.parseInt(st.nextToken());
        windowSize = Integer.parseInt(st.nextToken());

        List<Integer> visitors = Arrays.asList(br.readLine().split(" ")).stream().map(s -> Integer.parseInt(s))
                .collect(Collectors.toList());

        for (int i = 0; i < windowSize; i++) {
            sumOfVisitors += visitors.get(i);
        }
        maxVisitors = sumOfVisitors;
        count += 1;

        for (int i = 0; i < days - windowSize; i++) {
            sumOfVisitors -= visitors.get(i);
            sumOfVisitors += visitors.get(i + windowSize);

            if (maxVisitors < sumOfVisitors) {
                maxVisitors = sumOfVisitors;
                count = 1;
            } else if (maxVisitors == sumOfVisitors) {
                count += 1;
            }
        }

        if (maxVisitors == 0) {
            System.out.println("SAD");
            return;
        }
        System.out.println(maxVisitors);
        System.out.println(count);
    }
}