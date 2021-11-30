
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;				


public class CoinChange {

	public static void main(String[] args) {
        int[] coins = new int[] {1};
        int amount = 2;
        int ans = coinChange(coins, amount);
        System.out.println(ans);
        int act = 2;
        if (ans == act) {
        	System.out.println("Pass");
        }
	}
	
    public static int coinChange(int[] coins, int amount) {
    	int[] dp = new int[amount + 1];
    	Arrays.fill(dp, amount +1);
    	dp[0] = 0;
    	for (int i = 1; i <= amount; i ++) {
    		System.out.println(Arrays.toString(dp));
    		for (int c : coins) {
    			if ((i - c) >= 0 ) {
        			dp[i] = Collections.min(Arrays.asList(dp[i], 1 + dp[i - c]));
    			}
    		}
    	}
        return dp[amount] != amount + 1 ? dp[amount] : -1;
    }
}
