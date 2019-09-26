import java.util.Arrays;
import java.util.HashMap;

public class Solution {
    private HashMap <String, Integer> spokenWords = new HashMap<>();

    public int[] solution(int n, String[] words) {
        int wrongPerson = 0, numOfCycle = 0;

        if (words[0].length() == 1) {
            wrongPerson = 1;
            numOfCycle = 1;
        } else {
            spokenWords.put(words[0], 1);
            for (int i = 1; i < words.length; i++) {
                String currentWord = words[i];
                String previousWord = words[i - 1];
                if (currentWord.charAt(0) != previousWord.charAt(previousWord.length() - 1) || spokenWords.containsKey(currentWord) || currentWord.length() == 1) {
                    wrongPerson = (i + 1) % n == 0 ? n : (i + 1) % n;
                    numOfCycle = (i + 1) % n == 0 ? (i + 1) / n : ((i + 1) / n) + 1;
                    break;
                } else {
                    spokenWords.put(currentWord, i + 1);
                }
            }
        }
        int[] answer = {wrongPerson, numOfCycle};
        return answer;
    }

    public static void main(String[] args) {
        String[] test1 = {"tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"};
        System.out.println(Arrays.toString(new Solution().solution(3, test1)));
        String[] test2 = {"hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"};
        System.out.println(Arrays.toString(new Solution().solution(5, test2)));
        String[] test3 = {"hello", "one", "even", "never", "now", "world", "draw"};
        System.out.println(Arrays.toString(new Solution().solution(2, test3)));
        String a = "a";
        System.out.println(a.length());
    }
}
