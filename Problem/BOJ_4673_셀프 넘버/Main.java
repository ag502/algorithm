import java.io.*;

public class Main {
    public static int calcGenerator(int number) {
        int result = number;

        while (true) {
            int answer = number / 10;
            int remains = number % 10;

            number = answer;
            result += remains;

            if (answer == 0) {
                break;
            }
        }

        return result;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_4673_셀프 넘버\\input.txt"));

        boolean[] generators = new boolean[10001];

        for (int curNum = 1; curNum <= 10000; curNum++) {
            int result = calcGenerator(curNum);
            if (result > 10000) {
                continue;
            }
            generators[result] = true;
        }

        for (int curNum = 1; curNum <= 10000; curNum++) {
            if (!generators[curNum]) {
                System.out.println(curNum);
            }
        }
    }
}
