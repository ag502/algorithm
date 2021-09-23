import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_11053_가장 긴 증가하는 부분 수열\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numOfNumbers = Integer.parseInt(br.readLine());
        List<Integer> array = Arrays.stream(br.readLine().split(" ")).map(el -> Integer.parseInt(el))
                .collect(Collectors.toList());

        int[] partialLengths = new int[numOfNumbers];
        // 길이 1로 초기화
        for (int i = 0; i < numOfNumbers; i++) {
            partialLengths[i] = 1;
        }

        // dp
        for (int i = 1; i < numOfNumbers; i++) {
            for (int j = 0; j < i; j++) {
                if (array.get(i) > array.get(j)) {
                    partialLengths[i] = Math.max(partialLengths[i], partialLengths[j] + 1);
                }
            }
        }
        System.out.println(Arrays.stream(partialLengths).max().getAsInt());
    }
}