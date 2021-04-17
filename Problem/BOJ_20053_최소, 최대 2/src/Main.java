import java.util.*;
import java.io.*;


public class Main {
    static int testCase;
    static int numbersLength;
    static int[] numbers;
    static StringTokenizer st;
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        testCase = Integer.parseInt(br.readLine());

        for (int i = 0; i < testCase; i++) {
            numbersLength = Integer.parseInt(br.readLine());
            numbers = new int[numbersLength];
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < numbersLength; j++) {
                numbers[j] = Integer.parseInt(st.nextToken());
            }

            Arrays.sort(numbers);
            System.out.println(numbers[0] + " " + numbers[numbersLength - 1]);
        }
    }
}
