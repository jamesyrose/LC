
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;				


public class MostWater {

	public static void main(String[] args) {
        int[] nums = new int[]{1,8,6,2,5,4,8,3,7}; 
        int ans = maxArea(nums);
        System.out.println(ans);
        int act = 49;
        if (ans == act) {
        	System.out.println("Pass");
        }
	}
	
    public static int maxArea(int[] height) {
    	int l = 0 ; 
    	int r = height.length - 1;
    	int res = 0; 
    	int tmp = 0;
    	while (r > l) {
    		tmp = (r - l) * Math.min(height[l], height[r]); 
    		if (height[l] < height[r]) {
    			l++;
    		}else {
    			r--;
    		}
    		res = Math.max(tmp,  res);
    	}
    	return res;

    }
}
