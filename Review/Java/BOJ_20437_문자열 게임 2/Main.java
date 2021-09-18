import java.io.*;
import java.util.*;

public class Main {
    static int testCase;
    static StringTokenizer st;
    static HashMap<Character, ArrayList<Integer>> standardChar;
    public static void main(String[] args) throws IOException{
        System.setIn(new FileInputStream("Review\\Java\\BOJ_20437\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        testCase = Integer.parseInt(st.nextToken());

        for (int i = 0; i < testCase; i++) {
            int shortestStringLength = Integer.MAX_VALUE;
            int longestStringLength = Integer.MIN_VALUE;

            st = new StringTokenizer(br.readLine());
            String string = st.nextToken();
            
            st = new StringTokenizer(br.readLine());
            int windowSize = Integer.parseInt(st.nextToken());

            standardChar = new HashMap<>();

            for (int j = 0; j < string.length(); j++) {
                if (standardChar.get(string.charAt(j)) == null) {
                    standardChar.put(string.charAt(j), new ArrayList<Integer>());
                }
                standardChar.get(string.charAt(j)).add(j);
            }

            for (char key : standardChar.keySet()) {
                ArrayList<Integer> curIndexList = standardChar.get(key);
                if (curIndexList.size() >= windowSize) {
                    for (int k = 0; k < curIndexList.size() - windowSize + 1; k ++) {
                        shortestStringLength = Math.min(shortestStringLength, curIndexList.get(k + windowSize - 1) - curIndexList.get(k) + 1);
                        longestStringLength = Math.max(longestStringLength, curIndexList.get(k + windowSize - 1) - curIndexList.get(k) + 1);
                    }
                }
            }

            if (shortestStringLength == Integer.MAX_VALUE || longestStringLength == Integer.MIN_VALUE) {
                System.out.println(-1);
            } else {
                System.out.println(shortestStringLength + " " + longestStringLength);
            }
        }
    }
}    