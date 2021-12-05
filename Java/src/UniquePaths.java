class Solution {
    public int uniquePaths(int m, int n) {
        /*
        [  ,    ,    ,   ,  1],
        [  ,    ,    ,  3,  1],
        [ 5,   4,   3,  2,  1],
        [ 1,   1,   1,  1,  X],
        */
        
        int[][] dp = new int[m][n]; 
        for (int[] arr : dp){
            Arrays.fill(arr, 1);
        }
        
        for (int i = m - 2; i >= 0; i--){
            for (int j = n - 2; j >= 0; j--){
                dp[i][j] = dp[i][j + 1] + dp[i + 1][j]; 
            }
            
        } 
        
                
        return dp[0][0];
        
    }
}
