import java.util.*;
import java.io.*;


public class Main {
    static String dockHowling = "";
    static ArrayList<Stack<Character>> docks = new ArrayList<>();
    static int[] dockStack = new int[2500];
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("src\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        dockHowling = br.readLine();

        if (dockHowling.length() % 5 != 0) {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i < 2500; i++) {
            docks.add(new Stack<>());
        }

        for (int i = 0; i < dockHowling.length(); i++) {
            char curChar = dockHowling.charAt(i);
            for (int j = 0; j < dockStack.length; j++) {
                if (curChar == 'q' && dockStack[j] == 0) {
                    docks.get(j).push(curChar);
                    dockStack[j] = (dockStack[j] + 1) % 5;
                    break;
                } else if (curChar == 'u' && dockStack[j] == 1) {
                    docks.get(j).push(curChar);
                    dockStack[j] = (dockStack[j] + 1) % 5;
                    break;
                } else if (curChar == 'a' && dockStack[j] == 2) {
                    docks.get(j).push(curChar);
                    dockStack[j] = (dockStack[j] + 1) % 5;
                    break;
                } else if (curChar == 'c' && dockStack[j] == 3) {
                    docks.get(j).push(curChar);
                    dockStack[j] = (dockStack[j] + 1) % 5;
                    break;
                } else if (curChar == 'k' && dockStack[j] == 4) {
                    docks.get(j).push(curChar);
                    dockStack[j] = (dockStack[j] + 1) % 5;
                    break;
                }
            }
        }

        int answer = 0;
        int totalLength = 0;
        for (Stack<Character> stack : docks) {
            totalLength += stack.size();
            if (stack.size() != 0 && stack.size() % 5 == 0) {
                answer += 1;
            }
        }
        if (totalLength != dockHowling.length()) {
            System.out.println("-1");
            return;
        }
        System.out.println(answer == 0 ? -1 : answer);
    }
}
