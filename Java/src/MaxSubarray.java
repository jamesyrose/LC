
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;				


public class MaxSubarray {

	public static void main(String[] args) {
        int[] nums = new int[]{-2,1,-3,4,-1,2,1,-5,4}; 
        int ans = maxSum(nums);
        int act = 6;
        if (ans == act) {
        	System.out.println("Pass");
        }
	}
	
    public static int maxSum(int[] nums) {
    	int res = nums[0];
    	int cnt = 0; 
    	for (int n : nums) {
    		cnt = cnt + n; 
    		res = Math.max(cnt, res);
    		if (cnt < 0) {
    			cnt = 0; 
    		}
    	}
    	
		return res;
    }
}
