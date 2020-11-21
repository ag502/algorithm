import java.io.*;
import java.util.*;

public class Main {
    static int testCase = -1;

    public static void moveElement (Stack<String> st1, Stack<String> st2, int start, int end) {
        String startElem = st1.get(start - 1);
        String endElem = st1.get(end - 1);
        int stackLength = st1.size();

        for (int i = 0; i <= stackLength - Math.min(start, end); i++) {
            st2.push(st1.pop());
        }

        while (st2.size() != 0) {
            String curElem = st2.pop();

            if (curElem.equals(startElem)) {
                continue;
            }
            if (curElem.equals(endElem)) {
                st1.push(startElem);
            }
            st1.push(curElem);
        }
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<String> stack1 = new Stack<>();
        Stack<String> stack2 = new Stack<>();

        testCase = Integer.parseInt(br.readLine());
        for (int i = 0; i < testCase; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int numOfElem = Integer.parseInt(st.nextToken());
            int numOfOp = Integer.parseInt(st.nextToken());

            // 원소 집어 넣기
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < numOfElem; j++) {
                stack1.push(st.nextToken());
            }
            // 연산
            for (int j = 0; j < numOfOp; j++) {
                st = new StringTokenizer(br.readLine());
                int start = Integer.parseInt(st.nextToken());
                int end = Integer.parseInt(st.nextToken());
                moveElement(stack1, stack2, start, end);
            }
            System.out.println(stack1);
            stack1.clear();
            stack2.clear();
        }
    }
}
