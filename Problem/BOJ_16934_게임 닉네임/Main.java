import java.util.*;
import java.io.*;

class TrieNode {
    boolean isFinalNode;
    int count;
    Map<Character, TrieNode> children;

    public TrieNode() {
        this.count = 0;
        this.isFinalNode = false;
        this.children = new HashMap<>();
    }
}

class Trie {
    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public String insert(String str) {
        TrieNode curNode = this.root;

        StringBuilder subName = new StringBuilder("");
        boolean isAppendable = true;
        for (int idx = 0; idx < str.length(); idx++) {
            char curChar = str.charAt(idx);
            TrieNode findNode = curNode.children.get(curChar);

            // 이미 존재하는 경우
            if (findNode != null) {
                subName.append(curChar);
                curNode = findNode;
            } else {
                if (isAppendable) {
                    subName.append(curChar);
                    isAppendable = false;
                }
                TrieNode newNode = new TrieNode();
                curNode.children.put(curChar, newNode);
                curNode = newNode;
            }
        }
        curNode.isFinalNode = true;
        curNode.count++;

        return subName.toString() + "" + (curNode.count == 1 ? "" : curNode.count);
    }
}

public class Main {
    static int numOfNicknames;

    static Trie trie = new Trie();

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_16934_게임 닉네임\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        numOfNicknames = Integer.parseInt(br.readLine());
        for (int user = 0; user < numOfNicknames; user++) {
            String curNickname = br.readLine();
            String subName = trie.insert(curNickname);
            System.out.println(subName);
        }
    }
}