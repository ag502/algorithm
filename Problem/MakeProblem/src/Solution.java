public class Solution {
    private static boolean isPrime(int n) {
        double sqrtNum = Math.sqrt(n);
        for(int i = 2; i <= sqrtNum; i++) {
            if (n % i == 0) {
                return false;
            }
        }
        return true;
    }

    public int solution(int[] nums) {
        int sum;
        int numOfPrime = 0;
        for(int i = 0; i < nums.length - 2; i++) {
            for (int j = i + 1; j < nums.length - 1; j++) {
                for (int k = j + 1; k < nums.length; k++) {
                    sum = nums[i] + nums[j] + nums[k];
                    if (isPrime(sum)) {
                        numOfPrime++;
                    }
                }
            }
        }
        return numOfPrime;
    }

    public static void main(String[] args) {
        int[] test = {1, 2, 7, 6, 4};
        System.out.println(new Solution().solution(test));
    }
}
