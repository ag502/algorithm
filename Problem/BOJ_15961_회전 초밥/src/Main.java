import java.util.*;
import java.io.*;

public class Main {
    static int numOfPlates;
    static int numOfSushi;
    static int k;
    static int c;
    static StringTokenizer st;
    static int[] belt;
    static Map<Integer, Integer> curSushi = new HashMap<>();

    public static void main(String[] args) throws IOException {
	// write your code here
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        numOfPlates = Integer.parseInt(st.nextToken());
        numOfSushi = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        belt = new int[numOfPlates + k - 1];

        for (int i = 0; i < numOfPlates; i++) {
            belt[i] = (Integer.parseInt(br.readLine()));
        }

        for (int i = numOfPlates; i < belt.length; i++) {
            belt[i] = belt[i % numOfPlates];
        }

//        System.out.println(Arrays.toString(belt));
        curSushi.put(c, 1);

        for (int idx = 0; idx < k; idx++) {
            if (curSushi.containsKey(belt[idx])) {
                curSushi.put(belt[idx], curSushi.get(belt[idx]) + 1);
            } else {
                curSushi.put(belt[idx], 1);
            }
        }

//        for (int key: curSushi.keySet()) {
//            System.out.println(key + " = " + curSushi.get(key));
//        }

        int answer = curSushi.keySet().size();
//        System.out.println(answer);
        int start = 0, end = k - 1;


        while (true) {
            if (curSushi.get(belt[start]) - 1 == 0) {
                curSushi.remove(belt[start]);
            } else {
                curSushi.put(belt[start], curSushi.get(belt[start]) - 1);
            }
            start += 1;

            if (end >= belt.length - 1) {
                break;
            }
            end += 1;
            if (curSushi.containsKey(belt[end])) {
                curSushi.put(belt[end], curSushi.get(belt[end]) + 1);
            } else {
                curSushi.put(belt[end], 1);
            }

            answer = Math.max(answer, curSushi.keySet().size());
        }
        System.out.println(answer);
    }
}
