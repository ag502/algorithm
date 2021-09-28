import java.util.*;
import java.util.stream.*;
import java.io.*;

public class Main {
    static List<Integer> password;
    static int[] kindOfWords;

    public static int descryption(int passwordIdx) {
        if (passwordIdx < 0) {
            return 1;
        } else if (kindOfWords[passwordIdx] != 0) {
            return kindOfWords[passwordIdx];
        }

        int answer = 0;
        answer += descryption(passwordIdx - 1) % 1000000;

        int word = password.get(passwordIdx - 1) * 10 + password.get(passwordIdx);
        if (word <= 26) {
            answer += descryption(passwordIdx - 2) % 1000000;
        }
        kindOfWords[passwordIdx] = answer;
        return answer;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_2011_암호코드\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 암호 입력받기
        password = Arrays.stream(br.readLine().split("")).map(el -> Integer.parseInt(el)).collect(Collectors.toList());

        // dp 배열 초기화
        kindOfWords = new int[password.size()];
        kindOfWords[0] = 1;

        if (password.get(0) == 0) {
            System.out.println(0);
            return;
        }

        for (int i = 1; i < kindOfWords.length; i++) {
            if (password.get(i) != 0) {
                kindOfWords[i] += kindOfWords[i - 1];
            }
            if (i >= 1) {
                int curWord = password.get(i - 1) * 10 + password.get(i);
                if (0 < curWord && curWord <= 26) {
                    if (i < 2) {
                        kindOfWords[i] += 1;
                    } else {
                        kindOfWords[i] += kindOfWords[i - 2];
                    }
                }
            }
        }
        System.out.println(Arrays.toString(kindOfWords));
        System.out.println(kindOfWords[password.size() - 1]);
    }
}