import java.util.*;
import java.io.*;

public class Main {
    static String testString;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_16120_PPAP\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        testString = br.readLine();

        Stack<Character> stack = new Stack<>();
        // 문자열 역순으로 순회
        for (int idx = testString.length() - 1; idx >= 0; idx--) {
            char curChar = testString.charAt(idx);
            if (curChar == 'P') {
                // 스택의 길이가 3미만일때
                int curStackSize = stack.size();
                if (curStackSize < 3) {
                    stack.add(curChar);
                } else {
                    // 스택의 윗부분 3개가 PAP인지 검사
                    boolean isMatched = stack.get(curStackSize - 1) == 'P' && stack.get(curStackSize - 2) == 'A'
                            && stack.get(curStackSize - 3) == 'P';
                    if (isMatched) {
                        for (int count = 0; count < 3; count++) {
                            stack.pop();
                        }
                        stack.add('P');
                        while (true) {
                            curStackSize = stack.size();
                            if (curStackSize < 4) {
                                break;
                            }

                            isMatched = stack.get(curStackSize - 1) == 'P' && stack.get(curStackSize - 2) == 'P'
                                    && stack.get(curStackSize - 3) == 'A' && stack.get(curStackSize - 4) == 'P';

                            if (!isMatched) {
                                break;
                            }

                            for (int count = 0; count < 3; count++) {
                                stack.pop();
                            }
                            stack.add('P');
                        }
                    } else {
                        stack.add(curChar);
                    }
                }
            } else {
                stack.add(curChar);
            }
        }

        if (stack.size() == 1 && stack.firstElement() == 'P') {
            System.out.println("PPAP");
        } else {
            System.out.println("NP");
        }
    }
}