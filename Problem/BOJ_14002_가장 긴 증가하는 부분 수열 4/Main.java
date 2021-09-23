import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Main {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14002_가장 긴 증가하는 부분 수열 4\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int numOfNumbers = Integer.parseInt(br.readLine());
        List<Integer> array = Arrays.stream(br.readLine().split(" ")).map(el -> Integer.parseInt(el))
                .collect(Collectors.toList());

        int[] lenArray = new int[numOfNumbers];
        // 길이 배열 1로 초기화
        for (int i = 0; i < numOfNumbers; i++) {
            lenArray[i] = 1;
        }

        List<Deque<Integer>> queueList = new ArrayList<>();
        Deque<Integer> firstElQueue = new ArrayDeque<>();
        firstElQueue.offerFirst(array.get(0));
        queueList.add(firstElQueue);

        for (int i = 1; i < numOfNumbers; i++) {
            Deque<Integer> iThElQueue = new ArrayDeque<>();
            iThElQueue.offerFirst(array.get(i));
            queueList.add(iThElQueue);

            for (int j = 0; j < i; j++) {
                if (array.get(i) > array.get(j) && lenArray[i] < lenArray[j] + 1) {
                    lenArray[i] = lenArray[j] + 1;
                    Deque<Integer> jThElQueue = queueList.get(j);
                    Deque<Integer> newJThElQueue = new ArrayDeque<>(jThElQueue);
                    newJThElQueue.offerLast(array.get(i));
                    queueList.set(i, newJThElQueue);
                }
            }
        }

        int maxValue = Arrays.stream(lenArray).max().getAsInt();
        int maxIdx = 0;
        for (int i = 0; i < numOfNumbers; i++) {
            if (lenArray[i] == maxValue) {
                maxIdx = i;
                break;
            }
        }

        StringBuilder answer = new StringBuilder("");
        Deque<Integer> answerQueue = queueList.get(maxIdx);
        int size = answerQueue.size();

        for (int i = 0; i < size; i++) {
            if (i != size - 1) {
                answer.append(answerQueue.pollFirst() + " ");
                continue;
            }
            answer.append(answerQueue.pollFirst());
        }
        System.out.println(maxValue);
        System.out.println(answer);
    }
}
