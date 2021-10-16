import java.util.*;
import java.io.*;

public class Main {
    static char[] originString;
    static char[] dynamite;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_9935_문자열 폭발\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        originString = br.readLine().toCharArray();
        dynamite = br.readLine().toCharArray();

        Stack<Character> originStringStack = new Stack<>();
        Stack<Character> answerStringStack = new Stack<>();

        for (int idx = 0; idx < originString.length; idx++) {
            originStringStack.add(originString[idx]);
        }

        // 폭발물 탐지
        while (!originStringStack.empty()) {
            char curChar = originStringStack.pop();
            answerStringStack.add(curChar);
            if (curChar == dynamite[0]) {
                if (answerStringStack.size() >= dynamite.length) {
                    boolean isMatched = true;
                    // 다이너마이트와 일치하는지 판단
                    for (int idx = 0; idx < dynamite.length; idx++) {
                        if (dynamite[idx] != answerStringStack.get(answerStringStack.size() - 1 - idx)) {
                            isMatched = false;
                            break;
                        }
                    }
                    // 일치한다면 폭발
                    if (isMatched) {
                        for (int count = 0; count < dynamite.length; count++) {
                            answerStringStack.pop();
                        }
                    }
                }
            }
        }

        // 결과 출력
        StringBuilder answer = new StringBuilder("");
        while (!answerStringStack.empty()) {
            answer.append(answerStringStack.pop());
        }
        System.out.println(answer.length() == 0 ? "FRULA" : answer);
    }
}