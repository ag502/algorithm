import java.util.HashMap;

public class Solution {
    private HashMap<Character, Integer> skillMap = new HashMap<>();

    private void makeSkillMap(String skill) {
        for(int i = 0; i < skill.length(); i++) {
            skillMap.put(skill.charAt(i), i);
        }
    }

    public int solution(String skill, String[] skill_trees) {
        makeSkillMap(skill);
        int numOfPossible = 0;

        for(int i = 0; i < skill_trees.length; i++) {
            boolean isPossible = true;
            int existedSkillIndex = -1;

            for (int j = 0; j < skill_trees[i].length(); j++) {
                char currentSkill = skill_trees[i].charAt(j);
                int nextValue = existedSkillIndex + 1;
                if (skillMap.containsKey(currentSkill)){
                    if (existedSkillIndex > skillMap.get(currentSkill) || (nextValue != skillMap.get(currentSkill))) {
                        isPossible = false;
                        break;
                    }
                    existedSkillIndex = skillMap.get(currentSkill);
                }
            }
            if (isPossible) {
                numOfPossible++;
            }
        }
        return numOfPossible;
    }

    public static void main(String[] args) {
        String[] test1 = {"BACDE", "CBADF", "AECB", "BDA", "CB"};
        System.out.println(new Solution().solution("AB", test1));
    }
}
