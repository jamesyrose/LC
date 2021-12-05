class Solution {
    public int rob(int[] nums) {
        if (nums.length == 2){
            return Math.max(nums[0], nums[1]);
        }
        if (nums.length  == 1){
            return nums[0];
        }
        if (nums.length == 0 ){
            return -1;
        }
        int[] dp = new int[nums.length + 1]; 
        Arrays.fill(dp, 0); 
        
        for (int i = 0 ; i < nums.length; i++){
            int b1 = Math.max(0, i - 1); 
            int b2 = Math.max(0, i - 2);
            
            dp[i + 1] = Math.max(
                nums[i] + dp[b1], 
                nums[i] + dp[b2]
            );
        }
        return Math.max(dp[dp.length - 1 ], dp[dp.length - 2]); 
        
        
    }
}
