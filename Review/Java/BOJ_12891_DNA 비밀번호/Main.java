import java.util.*;
import java.io.*;

public class Main {
    static StringTokenizer st;
    static int answer = 0;
    static String[] standardDNA = {"A", "C", "G", "T"};

    static HashMap <String, Integer> standardDNACount;
    static HashMap <String, Integer> tempCount;

    public static boolean isPossible() {
        for (String key : tempCount.keySet()) {
            if (standardDNACount.get(key) > tempCount.get(key)) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Review\\Java\\BOJ_12891_DNA 비밀번호\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        int lengthOfDNA = Integer.parseInt(st.nextToken());
        int lengthOfPassword = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        String DNA = st.nextToken();

        st = new StringTokenizer(br.readLine());
        standardDNACount = new HashMap<>();
        for (int i = 0; i < standardDNA.length; i++) {
            if (standardDNACount.get(standardDNA[i]) == null) {
                standardDNACount.put(standardDNA[i], 0);
            }
            standardDNACount.put(standardDNA[i], Integer.parseInt(st.nextToken()));
        }

        tempCount = new HashMap<String, Integer>() {{
            put("A", 0);
            put("G", 0);
            put("T", 0);
            put("C", 0);
        }};

        for (int i = 0; i < lengthOfPassword; i++) {
            int curCount = tempCount.get(Character.toString(DNA.charAt(i)));
            tempCount.put(Character.toString(DNA.charAt(i)), curCount + 1);
        }
        if (isPossible()) {
            answer++;
        }

        for (int i = 0; i < lengthOfDNA - lengthOfPassword; i++) {
            int prevCount = tempCount.get(Character.toString(DNA.charAt(i)));
            tempCount.put(Character.toString(DNA.charAt(i)), prevCount - 1);

            int nextCount = tempCount.get(Character.toString(DNA.charAt(i + lengthOfPassword)));
            tempCount.put(Character.toString(DNA.charAt(i + lengthOfPassword)), nextCount + 1);
            if (isPossible()) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}