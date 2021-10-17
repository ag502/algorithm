import java.util.*;
import java.io.*;

class TrieNode {
    boolean isLastNode;
    String curString;
    Map<String, TrieNode> children;

    public TrieNode(String str) {
        this.isLastNode = false;
        curString = str;
        this.children = new HashMap<>();
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode("");
    }

    public void insert(String[] str) {
        TrieNode curNode = this.root;
        for (int idx = 0; idx < str.length; idx++) {
            String curString = str[idx];
            curNode = curNode.children.computeIfAbsent(curString, k -> new TrieNode(curString));
        }
        curNode.isLastNode = true;
    }

    public void dfs(TrieNode curNode, int depth) {
        if (curNode != this.root) {
            StringBuilder sb = new StringBuilder("");
            for (int i = 0; i < (depth - 1) * 2; i++) {
                sb.append("-");
            }
            sb.append(curNode.curString);
            System.out.println(sb);
        }

        Map<String, TrieNode> children = curNode.children;
        List<String> childrenKey = new ArrayList<>(children.keySet());
        Collections.sort(childrenKey, (s1, s2) -> s1.compareTo(s2));

        for (String key : childrenKey) {
            dfs(children.get(key), depth + 1);
        }
    }
}

public class Main {
    static int depthOfCave;
    static Trie trie = new Trie();

    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14725_개미굴\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        depthOfCave = Integer.parseInt(br.readLine());
        for (int depth = 1; depth <= depthOfCave; depth++) {
            st = new StringTokenizer(br.readLine());

            int lengthOfSignal = Integer.parseInt(st.nextToken());
            String[] signals = new String[lengthOfSignal];
            for (int i = 0; i < lengthOfSignal; i++) {
                signals[i] = st.nextToken();
            }

            // 신호 트라이에 삽입
            trie.insert(signals);
        }

        // 깊이 출력
        trie.dfs(trie.root, 0);
    }
}