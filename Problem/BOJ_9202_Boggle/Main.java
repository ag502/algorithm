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
    TrieNode root;

    public Trie() {
        this.root = new TrieNode();
    }

    public void insert(String str) {
        TrieNode curNode = this.root;

        for (int idx = 0; idx < str.length(); idx++) {
            char curChar = str.charAt(idx);
            curNode = curNode.children.computeIfAbsent(curChar, k -> new TrieNode());
        }
        curNode.isLastNode = true;
    }

    public TrieNode find(String str) {
        TrieNode curNode = this.root;

        for (int idx = 0; idx < str.length(); idx++) {
            TrieNode findNode = curNode.children.get(str.charAt(idx));

            if (findNode == null) {
                return findNode;
            }
            curNode = findNode;
        }
        return curNode;
    }
}

public class Main {
    static int[][] movingDir = { { -1, 0 }, { -1, 1 }, { 0, 1 }, { 1, 1 }, { 1, 0 }, { 1, -1 }, { 0, -1 }, { -1, -1 } };
    static int numOfDictWords;
    static int numOfBoards;

    static Trie trie = new Trie();
    static char[][] boggleBoard;
    static boolean[][] visited;
    static Set<String> wordList;

    public static int getScore(String str) {
        switch (str.length()) {
            case 1:
            case 2:
                return 0;
            case 3:
            case 4:
                return 1;
            case 5:
                return 2;
            case 6:
                return 3;
            case 7:
                return 5;
            default:
                return 11;
        }
    }

    public static void dfs(int curRow, int curCol, StringBuilder sb, int targetLen) {
        sb.append(boggleBoard[curRow][curCol]);
        visited[curRow][curCol] = true;

        if (sb.length() < targetLen) {
            for (int i = 0; i < movingDir.length; i++) {
                int nextRow = curRow + movingDir[i][0];
                int nextCol = curCol + movingDir[i][1];

                if (0 <= nextRow && nextRow < 4 && 0 <= nextCol && nextCol < 4) {
                    if (!visited[nextRow][nextCol]) {
                        dfs(nextRow, nextCol, sb, targetLen);
                    }
                }
            }
        }

        if (sb.length() == targetLen) {
            wordList.add(sb.toString());
        }
        sb.deleteCharAt(sb.length() - 1);
        visited[curRow][curCol] = false;
    }

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("Problem\\BOJ_9202_Boggle\\input.txt"));
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // input
        // 사전 단어 입력
        numOfDictWords = Integer.parseInt(br.readLine());
        for (int i = 0; i < numOfDictWords; i++) {
            trie.insert(br.readLine());
        }

        // 공백
        br.readLine();

        // boggle 보드 입력
        numOfBoards = Integer.parseInt(br.readLine());

        for (int i = 0; i < numOfBoards; i++) {
            int maxScore = 0;
            String longestWord = "";
            int numOfFindWord = 0;
            wordList = new HashSet<>();
            boggleBoard = new char[4][4];
            for (int row = 0; row < 4; row++) {
                boggleBoard[row] = br.readLine().toCharArray();
            }

            // dfs 1글자 -> 8글자
            visited = new boolean[4][4];
            for (int wordLength = 1; wordLength <= 8; wordLength++) {
                StringBuilder sb = new StringBuilder();
                for (int row = 0; row < 4; row++) {
                    for (int col = 0; col < 4; col++) {
                        if (!visited[row][col]) {
                            dfs(row, col, sb, wordLength);
                        }
                    }
                }
            }

            // 가능한 단어 조합 사전에서 찾기
            for (String curStr : wordList) {
                TrieNode findNode = trie.find(curStr);
                if (findNode != null && findNode.isLastNode) {
                    numOfFindWord += 1;
                    maxScore += getScore(curStr);
                    if (longestWord.equals("")) {
                        longestWord = curStr;
                    } else {
                        if (longestWord.length() < curStr.length()) {
                            longestWord = curStr;
                        } else if (longestWord.length() == curStr.length()) {
                            if (longestWord.compareTo(curStr) > 0) {
                                longestWord = curStr;
                            }
                        }
                    }
                }
            }

            System.out.println(maxScore + " " + longestWord + " " + numOfFindWord);

            br.readLine();
        }
    }
}