import java.util.*;
import java.io.*;

public class Main {
    static int numOfWords;
    static int maxLenOfWord;

    static StringTokenizer st;
    static Map<String, Integer> dictionary = new HashMap<>();

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_20920_영단어 암기는 괴로워\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        st = new StringTokenizer(br.readLine());
        numOfWords = Integer.parseInt(st.nextToken());
        maxLenOfWord = Integer.parseInt(st.nextToken());

        // 단어 입력
        for (int i = 0; i < numOfWords; i++) {
            String curWord = br.readLine();

            // 길이 m 이하인 단어 제외
            if (curWord.length() < maxLenOfWord) {
                continue;
            }

            int curWordCount = dictionary.getOrDefault(curWord, 0);
            dictionary.put(curWord, curWordCount + 1);
        }

        List<String> wordKeyList = new ArrayList<>(dictionary.keySet());
        Collections.sort(wordKeyList, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                int o1Count = dictionary.get(o1);
                int o2Count = dictionary.get(o2);
                if (o1Count < o2Count) {
                    return 1;
                } else if (o1Count > o2Count) {
                    return -1;
                } else {
                    if (o1.length() > o2.length()) {
                        return -1;
                    } else if (o1.length() < o2.length()) {
                        return 1;
                    } else {
                        return o1.compareTo(o2);
                    }
                }
            }
        });

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        for (String word : wordKeyList) {
            bw.write(word + "\n");
        }
        bw.close();
    }
}