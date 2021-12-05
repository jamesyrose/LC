class Solution {
    public int combinationSum4(int[] nums, int target) {
        Arrays.sort(nums);        
        int[] dp = new int[target + 1]; 
        Arrays.fill(dp, 0);
        dp[0] = 1; 
        
        for (int i = 0 ; i <= target; i ++){
            for (int val : nums){
                if (i - val >= 0 ){
                    dp[i] = dp[i] + dp[i - val];
                }
            }
        }
        
        
        
        
        
        return dp[target];
    }
}
