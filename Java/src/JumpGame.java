class Solution {
    public boolean canJump(int[] nums) {
        boolean[] dp = new boolean[nums.length];
        Arrays.fill(dp, false); 
        dp[nums.length - 1] = true; 
        
        for (int i = nums.length - 2 ; i >= 0; i--){
            boolean[] buff = Arrays.copyOfRange(dp, i, Math.min(i + nums[i] + 1, nums.length + 1));
            if (anyTrue(buff))
            {
                dp[i] = true;
            } 
        }
        return dp[0]; 
    }
    
    private boolean anyTrue(boolean[] tmp){
        for (boolean n : tmp){
            if (n){
                return true;
            }
        }
        return false;
    }
}

