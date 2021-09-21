import java.util.*;
import java.io.*;

class Truck {
    int weight;
    int entryTime;

    Truck(int weight, int entryTime) {
        this.weight = weight;
        this.entryTime = entryTime;
    }

    @Override
    public String toString() {
        return entryTime + " " + weight;
    }
}

public class Main {
    static int numOfTrucks;
    static int lenOfBridge;
    static int maxWeight;
    static int[] trucks;
    static Queue<Truck> queue;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_13335_트럭\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        numOfTrucks = Integer.parseInt(st.nextToken());
        lenOfBridge = Integer.parseInt(st.nextToken());
        maxWeight = Integer.parseInt(st.nextToken());

        // 트럭 배열 입력
        trucks = new int[numOfTrucks];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < numOfTrucks; i++) {
            trucks[i] = Integer.parseInt(st.nextToken());
        }

        // 다리 건너기
        queue = new LinkedList<>();
        int curIdx = 1;
        int time = 1;
        int curTotalWeight = trucks[0];

        queue.offer(new Truck(trucks[0], time));
        while (queue.size() != 0) {
            time++;
            // 나가는 트럭
            Truck outgoingTruck = queue.peek();
            if (outgoingTruck.entryTime + lenOfBridge == time) {
                queue.poll();
                curTotalWeight -= outgoingTruck.weight;
            }

            // 다리위에 올라간 트럭의 댓수가 다 찼을때
            if (queue.size() >= lenOfBridge) {
                continue;
            }

            // 무게 검사한 후 트럭 진입
            if (curIdx < numOfTrucks) {
                int inCommingTruck = trucks[curIdx];
                if (curTotalWeight + inCommingTruck <= maxWeight) {
                    queue.offer(new Truck(trucks[curIdx], time));
                    curTotalWeight += inCommingTruck;
                    curIdx++;
                }
            }
        }

        System.out.println(time);
    }
}
