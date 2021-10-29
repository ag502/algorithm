import java.util.*;
import java.io.*;

public class Main {
    static char[] operator = { '+', '-', ' ' };
    static List<List<Character>> opComb;
    static List<String> answer;

    public static void makeExpression(List<Character> op) {
        int curNum = 1;
        StringBuilder sb = new StringBuilder("");
        sb.append(curNum);
        for (char curOp : op) {
            curNum += 1;
            sb.append(curOp);
            sb.append(curNum);
        }

        char[] expression = sb.toString().replaceAll(" ", "").toCharArray();
        Stack<Integer> numberStack = new Stack<>();
        Stack<Character> opStack = new Stack<>();

        StringBuilder temp = new StringBuilder("");
        for (int i = 0; i < expression.length; i++) {
            if (Character.isDigit(expression[i])) {
                temp.append(expression[i]);
                continue;
            } else {
                numberStack.add(Integer.parseInt(temp.toString()));
                temp.setLength(0);

                if (opStack.isEmpty()) {
                    opStack.add(expression[i]);
                } else {
                    int secondNumber = numberStack.pop();
                    int firstNumber = numberStack.pop();

                    int result = 0;
                    char curOp = opStack.pop();
                    if (curOp == '+') {
                        result = firstNumber + secondNumber;
                        numberStack.add(result);
                    } else {
                        result = firstNumber - secondNumber;
                        numberStack.add(result);
                    }
                    opStack.add(expression[i]);
                }
            }
        }

        if (!opStack.isEmpty()) {
            char curOp = opStack.pop();
            int result = 0;

            if (curOp == '+') {
                result = numberStack.pop() + Integer.parseInt(temp.toString());
            } else {
                result = numberStack.pop() - Integer.parseInt(temp.toString());
            }

            if (result == 0) {
                answer.add(sb.toString());
            }
        }
    }

    public static void dfs(int curIdx, List<Character> temp, int targetCount) {
        temp.add(operator[curIdx]);

        if (temp.size() < targetCount) {
            for (int nextIdx = 0; nextIdx < operator.length; nextIdx++) {
                dfs(nextIdx, temp, targetCount);
            }
        }

        if (temp.size() == targetCount) {
            List<Character> newTemp = new ArrayList<>();
            newTemp.addAll(temp);
            makeExpression(newTemp);
            opComb.add(newTemp);
        }

        temp.remove(temp.size() - 1);
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_7490_0 만들기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        int testCase = Integer.parseInt(br.readLine());
        for (int t = 0; t < testCase; t++) {
            int maxNum = Integer.parseInt(br.readLine());
            opComb = new ArrayList<>();
            answer = new ArrayList<>();
            for (int idx = 0; idx < operator.length; idx++) {
                List<Character> temp = new ArrayList<>();
                dfs(idx, temp, maxNum - 1);
            }

            Collections.sort(answer, new Comparator<String>() {
                @Override
                public int compare(String s1, String s2) {
                    return s1.compareTo(s2);
                }
            });

            for (String expression : answer) {
                System.out.println(expression);
            }

            if (t != testCase - 1) {
                System.out.println("");
            }
        }
    }
}