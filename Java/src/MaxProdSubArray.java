
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;				


public class MaxProdSubArray {

	public static void main(String[] args) {
        int[] nums = new int[]{2,3,-2,4}; 
        int ans = maxProduct(nums);
        int act = 6;
        if (ans == act) {
        	System.out.println("Pass");
        }
	}
	
    public static int maxProduct(int[] nums) {
    	int maxVal = 1; 
    	int minVal = 1;
    	int tmp = 1; 
    	int res = Arrays.stream(nums).max().getAsInt();
    	
    	for (int n: nums) {
    		if (n == 0 ) {
    			maxVal = 0;
    			minVal = 0;
    		}else {
    			tmp = maxVal; 
    			maxVal =  Collections.max(Arrays.asList(n, maxVal * n, minVal * n));
    			minVal =  Collections.min(Arrays.asList(n, tmp * n, minVal * n));
        		res = Math.max(maxVal, res);
    		}

    	}
		return res;
    }
}
