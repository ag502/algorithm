import java.util.*;
import java.io.*;

class TrieNode {
    boolean isLastNode;
    Map<Character, TrieNode> children;

    public TrieNode() {
        this.isLastNode = false;
        this.children = new HashMap<>();
    }
}

class Trie {
    TrieNode rootNode;

    public Trie() {
        this.rootNode = new TrieNode();
    }

    public void insert(String str) {
        TrieNode curNode = this.rootNode;
        for (int idx = 0; idx < str.length(); idx++) {
            char curChar = str.charAt(idx);
            curNode = curNode.children.computeIfAbsent(curChar, k -> new TrieNode());
        }

        curNode.isLastNode = true;
    }

    public TrieNode find(String str) {
        TrieNode curNode = this.rootNode;

        for (int idx = 0; idx < str.length(); idx++) {
            char curChar = str.charAt(idx);

            TrieNode findNode = curNode.children.get(curChar);
            if (findNode == null) {
                return findNode;
            }
            curNode = findNode;
        }

        return curNode;
    }
}

public class Main {
    static int numOfStringSet;
    static int numOfCheckedString;

    static Trie trie = new Trie();

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_14426_접두사 찾기\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        StringTokenizer st = new StringTokenizer(br.readLine());
        numOfStringSet = Integer.parseInt(st.nextToken());
        numOfCheckedString = Integer.parseInt(st.nextToken());

        // 문자열 집합으로 트라이 구성
        for (int i = 0; i < numOfStringSet; i++) {
            trie.insert(br.readLine());
        }

        // 검사해야할 문자 입력
        int answer = 0;
        for (int i = 0; i < numOfCheckedString; i++) {
            TrieNode findNode = trie.find(br.readLine());
            if (findNode != null) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}