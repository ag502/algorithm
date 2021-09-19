import java.util.*;
import java.io.*;

public class Main {
    static int[] originalChars;
    static int[] passwordChars;
    static String original;
    static String password;
    static boolean flag = false;

    public static boolean isPossible() {
        for (int i = 0; i < original.length(); i++) {
            char curChar = original.charAt(i);
            if (originalChars[curChar - 'a'] != passwordChars[curChar - 'a']) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_9549_암호화된 비밀번호\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        for (int t = 0; t < testCase; t++) {
            flag = false;
            password = br.readLine();
            original = br.readLine();

            int originalLen = original.length();

            // 원래 암호문 알파벳 갯수 카운트
            originalChars = new int[26];
            for (int i = 0; i < originalLen; i++) {
                originalChars[original.charAt(i) - 'a'] += 1;
            }

            // 암호화된 암호문 알파벳 갯수 카운트
            passwordChars = new int[26];
            for (int i = 0; i < originalLen; i++) {
                passwordChars[password.charAt(i) - 'a'] += 1;
            }

            if (isPossible()) {
                System.out.println("YES");
                continue;
            }

            // 슬라이딩 윈도우
            for (int i = 0; i < password.length() - originalLen; i++) {
                // 윈도우 맨 앞 빼기
                passwordChars[password.charAt(i) - 'a'] -= 1;
                // 윈도우 맨 뒤 빼기
                passwordChars[password.charAt(i + originalLen) - 'a'] += 1;

                if (isPossible()) {
                    System.out.println("YES");
                    flag = true;
                    break;
                }
            }

            if (flag) {
                continue;
            }
            System.out.println("NO");
        }
    }
}