import java.util.*;
import java.io.*;

public class Main {
    static int numOfCommands;

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_11723_집합\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfCommands = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder("");
        int set = 0;

        for (int command = 0; command < numOfCommands; command++) {
            st = new StringTokenizer(br.readLine());
            String curCommand = st.nextToken();
            int number = -1;
            if (!curCommand.equals("all") && !curCommand.equals("empty")) {
                number = Integer.parseInt(st.nextToken());
            }

            // 명령어 처리
            switch (curCommand) {
                case "add":
                    int addNumber = 1 << (number - 1);
                    set |= addNumber;
                    break;
                case "remove":
                    int removeNumber = ~(1 << (number - 1));
                    set &= removeNumber;
                    break;
                case "check":
                    boolean check = (set & (1 << (number - 1))) != 0;
                    sb.append(check ? 1 : 0).append('\n');
                    break;
                case "toggle":
                    set ^= 1 << (number - 1);
                    break;
                case "all":
                    set = (1 << 20) - 1;
                    break;
                case "empty":
                    set = 0;
                    break;
            }
        }

        System.out.println(sb);
    }
}